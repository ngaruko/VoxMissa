from unicodedata import name
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.events, name="events"),
    path('event/<str:pk>/', views.event, name="event"),
    path('registration-confirmation/<str:pk>/', views.registration_confirmation, name="registration-confirmation"),
    path('proposal-submission/<str:pk>/', views.proposal_submission, name="proposal-submission"),


]