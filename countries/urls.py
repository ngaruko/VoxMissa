from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [

    path('', views.countries, name="countries"),
    path('<str:code>/', views.country, name="country"),

    path('<str:code>/parties/', include('parties.urls')),

    path('<str:code>/projects/', include('projects.urls')),
    path('<str:code>/policies/', include('policies.urls')),
    path('<str:code>/candidates/', include('forum.urls')),
    path('<str:code>/forum/', include('forum.urls')),
   
]
