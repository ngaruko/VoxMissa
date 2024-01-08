from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [

    path('', views.countries, name="countries"),
    path('<str:country>/', views.country, name="country"),
    path('<str:country>/projects/', include('projects.urls')),
    path('<str:country>/policies/', include('policies.urls')),
    path('<str:country>/candidates/', include('forum.urls')),
    path('<str:country>/forum/', include('forum.urls')),
   
]
