#render function gives response based on data from view
from django.shortcuts import render

#view takes info from request, prepares and sends data for page
#uses template to define what page will look like

# Create your views here.

#after home page path is matched to requested URL...
#django looks for index in views
#index takes requested argument and generates response (render)
    #.html is template response to request
def index(request):
    """home page for Learning Log"""
    return render(request, "learning_logs/index.html")
