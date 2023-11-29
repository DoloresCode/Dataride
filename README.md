# DataRide

## Description

DataRide is an innovative web application designed to visualize and analyze bike trip data. It enables users to query trip data based on station ID and view comprehensive trip details. DataRide is ideal for urban planners, cyclists, and data enthusiasts interested in bike-sharing systems.

The application features a user-friendly interface for querying data and provides API endpoints for accessing trip information. It leverages a robust backend built with Django and a PostgreSQL database to handle large datasets efficiently.

Key Features:

### Data Visualization
- **Interactive API Testing**: Users can test the API directly from the website by inputting a station ID and specifying the number of entries to retrieve.
- **Trip Data Display**: The application displays detailed trip data including start and end times, duration, station information, bike ID, user type, and more.

### Data Query API
- **TripData API**: Users can query trip data based on station ID with optional parameters for the number of entries. The API returns data in a structured JSON format.

### User-Friendly Interface
- **Home Page**: Introduces the app and its purpose.
- **About Page**: Provides information about the app, its usage, and the developer.
- **API Tester**: An interactive form where users can input parameters to test the API.
- **API Results**: Displays the results of the API query in a clear, tabulated format.


### Images

<img width="894" alt="Dataride_homepage" src="https://github.com/DoloresCode/Dataride/assets/117631390/cf854b42-3cf4-4871-a890-b4776b621c67">

<img width="740" alt="Dataride_api_tester" src="https://github.com/DoloresCode/Dataride/assets/117631390/c7531ebd-b014-4d15-90a6-e3980243a39a">

<img width="999" alt="Dataride_results" src="https://github.com/DoloresCode/Dataride/assets/117631390/4bf35505-f772-4af1-b2fa-a955cb04881e">


## Getting Started

# Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- You have  a macOS machine
- pipenv installed (pip install pipenv)
- Virtualenv (optional but recommended for creating isolated Python environments)

# Installation

1. **Clone the Repository:**

- git clone https://github.com/DoloresCode/Dataride.git

- cd Dataride/dataride_project

2. **Set up a Virtual Environment (create and activate):**

- pipenv install
- pipenv shell

3. **Initialize the Database:**

- python manage.py makemigrations
- python manage.py migrate

4. **Run the Server:**

- python manage.py runserver or python3 manage.py runserver

7. **Access the Application:**

- Open your web browser and go to `http://127.0.0.1:8000/`.

## Technologies and Tools Used

**Front-End**
- HTML/CSS/JavaScript
- Bootstrap for styling

**Back-End**
- Python with Django
- PostgreSQL Database

**Data Source**
- Bike trip data in CSV format

**Development Tools**
- Git and GitHub for version control
- Virtualenv for Python environment management

## Data Source

The bike trip data used in this application is sourced from a CSV file containing comprehensive trip records. 

## How It Works

1. Users visit the DataRide web application.
2. On the API Tester page, users input a station ID and the number of entries they wish to query.
3. The application processes the request and displays the results on the API Results page.
4. Users can view detailed trip information in a tabulated format.

## Potential Use Cases

DataRide is valuable for:
- Urban transportation planning and analysis.
- Cyclists looking to understand bike-sharing usage patterns.
- Data analysts and enthusiasts interested in urban mobility studies.

## Future Enhancements

- [ ] **Map Integration**: Displaying trip start and end points on an interactive map.
- [ ] **Advanced Filtering**: Allowing users to filter data based on time, date, and other criteria.
- [ ] **Data Analytics**: Implementing features for data analytics and visualizations.
- [ ] **User Account System**: Enabling users to save queries and access historical data.


## About the Developer

DataRide is developed by Dolores Crazover, a passionate full-stack developer with a keen interest in data-driven web applications. Connect with Dolores on [GitHub](https://github.com/DoloresCode) or [LinkedIn](https://www.linkedin.com/in/dolores-crazover/).
