from django.shortcuts import render
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
    return render(request, 'api-results.html')