from django.db import models
from django.contrib.auth.models import User

#define a model(class)
#tells us what to do with data
#define a model for every Topic users store
#Parent Model class defines a models functionality
class Topic(models.Model):
    """A topic the user is learning about"""

    #attribute for text, CharField is characer/text object
    #max amount of characters is 200
    text = models.CharField(max_length=200)

    #DateTimeField records date and time
    #argument auto_now_add means record current
    # time when user adds a topic
    date_added = models.DateTimeField(auto_now_add=True)

    #attribute of owner, which has relationship with topic
    #ForeignKey = User(owner) is key, Topics are values
    #User is default model
    #CASCADE = if user is deleted, so are topics
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    #method that converts object to string automatically
    def __str__(self):
        """Return a string representation of the model"""
        return self.text


#Entry inherits from djangos Model class
class Entry(models.Model):
    """Something specific learned about a topic"""

    #topic attribute is reference to Topic
    #foreign key connects each entry to specfic topic
    #each topic has ID/key
    #Cascade argument means that when a topic is deleted so
    # are all entries
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    #text attribute different from that of Topic
    #no size limit like Charfield
    text = models.TextField()

    #same attribute defined as in Topic
    date_added = models.DateTimeField(auto_now_add=True)

    #nested class
    #Meta holds extra info for models
    #use Entries when referriing to more than one entry
    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        "Return a string representation of the model"

        #this refers to the admin interface
        #convert text to string
        #only show first 50 characters of string in admin interface
        return f"{self.text[:50]}..."