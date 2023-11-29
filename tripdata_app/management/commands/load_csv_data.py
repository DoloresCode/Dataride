import csv #Python's built-in csv module, which provides functionality for reading and writing CSV files
from django.core.management.base import BaseCommand #Python's base command class for writing management commands
from django.utils.dateparse import parse_datetime #Python's dateparse module, which provides functionality for parsing dates and times from strings into Python datetime objects
from tripdata_app.models import TripData #our TripData model 

class Command(BaseCommand):
    help = 'Load CSV data into the dataride_db' #description of the command

    #description of the command's arguments parser (the parser is used to parse the command line arguments passed to the command) and the argument is the name of the CSV file (with its path) to load into the database file 
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    #the handle() method is called when the command is run
    #the path to the CSV file is stored in the csv_file_path variable
    def handle(self, *args, **kwargs): 
        csv_file_path = kwargs['csv_file'] 
        

        #open the CSV file in read mode 
        #DictReader is a class that reads rows from a CSV file into a dictionary
        #list to store TripData objects before bulk creation
        with open(csv_file_path, 'r') as file: 
            reader = csv.DictReader(file) 
            trip_data_list = [] 

            #iterate over the rows of the CSV file and create a TripData object for each row
            #append the TripData object to the trip_data_list
            #after the iteration is complete, bulk create the TripData objects in the database
            for row in reader:

                # Convert 'end station id' to int if it's a nbr, otherwise put None/'NULL'
                end_station_id = row['end station id']
                if end_station_id and end_station_id.isdigit():
                    end_station_id = int(end_station_id)
                else:
                    end_station_id = None

                # handle 'NULL' or empty values for 'end_station_name'
                end_station_name = row['end station name']
                if end_station_name in [None, '', 'NULL']:
                    end_station_name = None

                # handle potential 'NULL' or non-numeric values for latitude & longitude
                def parse_float(value):
                    if value in [None, '', 'NULL']:
                        return None
                    else:
                        return float(value)
                
                end_station_latitude = parse_float(row['end station latitude'])
                end_station_longitude = parse_float(row['end station longitude'])

                #Convert birth year to integer if it is a nbr, otherwise set it to None/Null
                birth_year = row['birth year']
                if birth_year.isdigit():
                    birth_year = int(birth_year)
                else:
                    birth_year = None

                trip_data = TripData(
                    trip_duration=int(row['tripduration']),
                    start_time=parse_datetime(row['starttime']),
                    stop_time=parse_datetime(row['stoptime']),
                    start_station_id=int(row['start station id']),
                    start_station_name=row['start station name'],
                    start_station_latitude=float(row['start station latitude']),
                    start_station_longitude=float(row['start station longitude']),
                    end_station_id=end_station_id,
                    end_station_name=end_station_name,
                    end_station_latitude=end_station_latitude,
                    end_station_longitude=end_station_longitude,
                    bikeid=int(row['bikeid']),
                    usertype=row['usertype'],
                    birth_year=birth_year,
                    gender=int(row['gender'])
                )
                trip_data_list.append(trip_data)

            TripData.objects.bulk_create(trip_data_list)

        #print a success message to the console
        self.stdout.write(self.style.SUCCESS('Data successfully loaded into database.🚴🏼🔥🔥🔥🔥🔥🚴🏼'))
