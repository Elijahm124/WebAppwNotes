#view takes info from request, prepares and sends data for page
#uses template to define what page will look like

#render function gives response based on data from view
#redirect function redirects user to specific page(view)
from django.shortcuts import render, redirect

#this function necessitates that a user is logged in to view the page
#each function represents a view for a page so its before a function
from django.contrib.auth.decorators import login_required

#used to return a 404 error page
from django.http import Http404

#import models associated with data we need
#import Entry model because working with existing entry
from .models import Topic, Entry

#import forms associated with data we need
from .forms import TopicForm, EntryForm

#index is called in urls.py
#argument is request object received from server
#index takes requested argument and generates response (render)
 #.html is template response to request
def index(request):
    """home page for Learning Log"""
    return render(request, "learning_logs/OGindex.html")

#view page for all topics

#login required = function that requires user is logged in
#always placed before view function
#ensures that specific topics are only seen by specfic user
#also takes care of entries cuz its apart of topics
#if user not logged in we send specific URL request
# (go to diff specific page instead)
@login_required()
def topics(request):
    """Show all topics"""

    #variable for database of topics is retreived and sorted
    #attribute is based off Topic model
    #date_added is attribute of Topic class
    #filter(owner) function
        #only when current user matches owner = access to owner's topics
        #basically correlates current user to their topics
    topics =  Topic.objects.filter(owner=request.user).order_by("date_added")


    #context is dictionary of name and data
    #key is topics, value is queryset of topics
    #data is sent to template for use
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


#topic_id is a new argument
#topic id accepts topic_id value integer from urls.py
@login_required()
def topic(request, topic_id):

    #.get() retrieves topics
    topic =Topic.objects.get(id = topic_id)

    # Make sure topic belongs to current user
    # although topics attribute matches a user to their topics...
        # any user would still have access to topics thru URL
    # this if statement ensures user is owner of topics before showing pagge
    #wont show entries for specfic topic if user isnt owner of topic
    if topic.owner != request.user:

        # error page
        # raise = create an exception and do action
        raise Http404

    #retrieves entries for each topic(above variable)
    #order entry set, reverse denoted by minus sign (most recent)
    entries = topic.entry_set.order_by("-date_added")

    #store topic and entries for each topic in context dict
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/OGtopic.html", context)

#GET request = need info (blank page)
#POST request = need to give info
@login_required()
def new_topic(request):
    """Add a new topic"""

    #request is GET, so we need info (blank page)
    if request.method != "POST":

        #no data submitted; create a blank form
        #create an instance of TopicForm(blank page)
        form = TopicForm()

    #else means if request.method is POST
    #processes data submitted in form
    else:

        #instance of form which has data stored in request.POST
        #POST data submitted; process data
        form = TopicForm(data=request.POST)

        #check if form Topic has everything needed (all fields)
        #is TOpic class and is TOpicForm class satisfied
        if form.is_valid():

            #these 3 lines match a new_topic to current user
                #like how new entry matches to current topic
            # writes data from form to database
            #also sets to variable new_topic
            new_topic = form.save(commit=False)

            #attribute for new_topic.owner is set to match current user
            new_topic.owner = request.user

            #saves new_topic and the user that its matched with
            new_topic.save()


            #redirect to topics page after finished creating a topic
            return redirect("learning_logs:topics")


    #display blank or invalid form
    #blank form gets sent as variable in context dict
    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)

#topic_id is parameter cuz we want to match it with value from URL
@login_required()
def new_entry(request, topic_id):
    """Add a new entry for a particular topic"""

    #variable is retrieved topic from Topics with matching id to URL id
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":

        #GET method = we need to sumbit data, create empty form instance
        #No data submitted, create blank form
        form = EntryForm()

    else:
        #POST data submitted; process data
        #inctance of EmptyForm with posted data
        form = EntryForm(data=request.POST)


        if form.is_valid():

            #newly created entry object
            #commit =False means dont save to database yet
            new_entry = form.save(commit=False)

            #topic value for new_entry object is topic from start of function
            #ensures topic value correlates with entry value
            new_entry.topic = topic

            #saves new entry to database
            new_entry.save()

            #takes us to different view page
            #main page for specific topic with specific id
            return redirect("learning_logs:topic", topic_id=topic_id)

    #Display a blank or invalid form
    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)

@login_required()
def edit_entry(request, entry_id):
    """Edit an existing entry"""

    #get entry object that will be edited
    #entry object has id matching entry_id specified in URL request
    entry = Entry.objects.get(id=entry_id)

    #get topic associated with entry
    topic = entry.topic

    #another way other users would have access to others' entries
    if topic.owner != request.user:
        raise Http404

    #GET request, instead of empty form we call requested entry to edit
    if request.method != "POST":

        #create form with info from called/existing entry
        #Intitial request;
        form = EntryForm(instance=entry)

    else:
        #POST data submitted; process data
        #modify form with initial entry as base and request.POST as new data
        #basically creates a form combining OG form and new input
        form = EntryForm(instance=entry, data=request.POST)

        #entry is already associated with topic
        # we dont need arguments like new_entry view
        if form.is_valid():
            form.save()

            #return to specific topic page
            return redirect("learning_logs:topic", topic_id=topic.id)

    #context dict, we need all these keys and its values for HTML
    context = {"entry": entry, "topic": topic, "form": form}

    #generate template
    return render(request, "learning_logs/edit_entry.html", context)
