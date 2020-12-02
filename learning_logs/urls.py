#make a set of defined URLs for learning_logs app
"""Defines URL patterns for learning_logs"""

#path function used when mapping URLs to views
from django.urls import path

#(.) means that views is from same directory as urls
from . import views

#specifies that this urls.py file is for learning_logs
app_name = "learning_logs"

#individual pages that can be used from learning logs app
#basically its a subset of pages specifically for this app
urlpatterns = [

#Home page
    #path function takes 3 arguments
    #1. string to route request to match a view
        #empty string matches local base URL
    #2. which function to call in views.py when match is made
    #3. proides name for URL pattern, replaces actual URL
    path('', views.index, name = 'index'),
]
