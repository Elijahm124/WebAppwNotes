from django.contrib import admin

# Register your models here.

#import class Topic from models
#its dot models cuz models is in same directory as admin
from .models import Topic, Entry

#register and allow managing of model thru admin site
admin.site.register(Topic)
admin.site.register(Entry)


