from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from . import views
from eventcalendar.views import DashboardView


urlpatterns = [
    path("dashboard", DashboardView.as_view(), name="dashboard"),
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('policies/', include('policies.urls')),
    path('parties/', include('parties.urls')),
    path('candidates/', include('forum.urls')),
    path('forum/', include('forum.urls')),
    path('users/', include('users.urls')),
    path('calendar/', include('eventcalendar.urls')),
    path('api/', include('api.urls')),

    #this has to be last. Poor design I know, but I am working on it
    path('seed', views.seed, name="home"),
    path('', views.home, name="home"),
    path('<str:pk>/', views.country, name="country"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"),
         name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"),
         name="password_reset_complete"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# 1 - User submits email for reset              //PasswordResetView.as_view()           //name="reset_password"
# 2 - Email sent message                        //PasswordResetDoneView.as_view()        //name="passsword_reset_done"
# 3 - Email with link and reset instructions    //PasswordResetConfirmView()            //name="password_reset_confirm"
# 4 - Password successfully reset message       //PasswordResetCompleteView.as_view()   //name="password_reset_complete"
