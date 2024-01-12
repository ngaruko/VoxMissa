from django.urls import path
from . import views

urlpatterns = [
    path('', views.policies, name="policies"),
    path('policy/<str:policy_id>/', views.policy, name="policy"),
    path('policy/<str:policy_id>/subtopics', views.subtopics, name="subtopics"),
    path('policy/<str:policy_id>/subtopics/subtopic/<str:subtopic_id>/', views.subtopic, name="subtopic"),

    path('create-policy/', views.createPolicy, name="create-policy"),

    path('update-policy/<str:pk>/', views.updatePolicy, name="update-policy"),

    path('delete-policy/<str:pk>/', views.deletePolicy, name="delete-policy"),
]
