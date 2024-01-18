from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('projects/<str:pk>/', views.getProject),
    path('projects/<str:pk>/vote/', views.projectVote),

    #policies
    path('policies/', views.getPolicies),
    path('policies/<str:pk>/', views.getPolicy),
    # path('policies/<str:pk>/vote/', views.policyVote),

    #parties
    path('parties/', views.getParties),
    path('parties/<str:pk>/', views.getParty),
    # path('parties/<str:pk>/vote/', views.partyVote),

    path('remove-tag/', views.removeTag)
]
