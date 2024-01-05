from django.urls import path
from . import views

urlpatterns = [
    path('', views.policies, name="policies"),
    path('party/<str:party_id>/', views.party, name="party"),
    path('party/<str:party_id>/subtopics', views.subtopics, name="subtopics"),
    path('party/<str:party_id>/subtopics/subtopic/<str:subtopic_id>/', views.subtopic, name="subtopic"),

    path('create-party/', views.createPolicy, name="create-party"),

    path('update-party/<str:pk>/', views.updatePolicy, name="update-party"),

    path('delete-party/<str:pk>/', views.deletePolicy, name="delete-party"),
]