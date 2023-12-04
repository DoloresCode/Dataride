from django.shortcuts import render
from django.http import Http404
#from django.views import View 
# from django.http import HttpResponse #text response
from django.views.generic.base import TemplateView #html response
from .models import TripData

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'


def interactive_form(request):
    return render(request, 'api-tester.html')


def api_results(request):
    # retrive query parqmeteres (station id and if no provided default empty string + nbr of entries of 10 by default) from the request.
    station_id = request.GET.get('station_id', '')
    number_of_entries = request.GET.get('number_of_entries', 10)

    # we initialize an empty list of trips to store the trip data (results) we will fetch from the database.
    trips = []

    if station_id:
        try:
            station_id = int(station_id) # convert station_id to integer
        except ValueError:
            raise Http404("Invalid input: station ID must be an integer.") #if no possible to convert to integerreturn value error

        # Get number_of_entries from request, default to 10 if not provided or not an integer
        number_of_entries = request.GET.get('number_of_entries', 10)
        try:
            number_of_entries = int(number_of_entries)
        except ValueError:
            number_of_entries = 10  # Default to 10 if conversion fails

        # Query the database for the first 10 trips that start at the station with the given station_id. It uses Django’s ORM (Object-Relational Mapping) to interact with the database.
        trips = TripData.objects.filter(start_station_id=station_id)[:number_of_entries]
    
    # render the response
    return render(request, 'api-results.html', {'station_id': station_id, 'data': trips})

