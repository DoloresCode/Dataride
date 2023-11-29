from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('api-tester/', views.interactive_form, name="api-tester"),
    path('api-results/', views.api_results, name="api-results"),
]