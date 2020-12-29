"""Defines URL patterns for users"""

#path function provides path from URL to view
#view function allows us to call default django authentication URL
from django.urls import path, include

from . import views

#can distinguish URLs from other apps (learning_logs)
app_name = "users"

urlpatterns = [

    #include default auth urls
    #login page, calls django's default login/logout views
    #we don't have to create a view for this page request
    path("", include("django.contrib.auth.urls")),

    #registration page
    #there is no default registration view so we import views
    #URL is base for users app + register
    path("register/", views.register, name="register"),


]