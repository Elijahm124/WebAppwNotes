"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


#manage URLs for admin site
from django.contrib import admin

#path module mathcess URLs to views
from django.urls import path, include

#list of URLs from all apps in the project
urlpatterns = [

    #admin.site.urls defines all URLs that can be requested from admin site
    #this is the path for the admin site
    #When URL is followed by admin/ brings us to admin site
    path('admin/', admin.site.urls),

    #URLs for users app
    #users app contains all stuff working with users(registration, authorization)
    #users app URL is base + users/
    #imports/calls users app (users.urls)
    path('users/', include("users.urls")),

    #URLs for learning_logs app
    #imports module/file learning_logs.urls
    #base URL calls learning_logs.urls
    path('', include("learning_logs.urls")),


]
