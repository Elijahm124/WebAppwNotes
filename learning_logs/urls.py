"""Defines URL patterns for learning_logs"""

#maps/matches URLs to views
from django.urls import path

#(.) means that views is from same directory as urls
from . import views

#specifies that this urls.py file is for learning_logs
app_name = "learning_logs"

#individual pages that can be requested from learning logs app
#subset of pages specifically for this app
urlpatterns = [

#Home page
    #3 arguments
    #1. string to route request to match a view
        #empty string matches local base URL
    #2. which function to call in views.py when match is made
        #index function
    #3. alternate name for URL pattern, replaces actual URL
    path('', views.index, name = 'index'),

#page that shows all topics
    #base URL + topics/ will be url to match to get template
    #calls views.topics
    path("topics/", views.topics, name="topics"),

#page for a single topic
    #each topic will have its own page, based on view, url, & template
    #base URL + topics + id
    #<>, matches integer value to topic_id
    #topic id will be matched to specific topic
    path("topics/<int:topic_id>/", views.topic, name = "topic"),

#page for adding a new topic
    path("new_topic/", views.new_topic, name ="new_topic"),

#page for adding a new entry
#topic id is included cuz we're adding an entry for a specific topic
#topic_id thus has to match number specified
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),

#page for editing an entry
#each entry has an id number and is in a queryset for a specific topic
#topic.entry_set.get(id))
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),

]
