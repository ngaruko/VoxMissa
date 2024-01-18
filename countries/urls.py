from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [

    path('', views.countries, name="countries"),
    path('<str:pk>/', views.country, name="country"),

    # path('<str:pk>/parties/', include('parties.urls')),

    # path('<str:pk>/projects/', include('projects.urls')),
    # path('<str:pk>/policies/', include('policies.urls')),
    # path('<str:pk>/candidates/', include('forum.urls')),
    # path('<str:pk>/forum/', include('forum.urls')),
   
]
