from django.shortcuts import render, redirect

#log user in if registration info is correct
from django.contrib.auth import login

#default form for registering a new user
from django.contrib.auth.forms import UserCreationForm

#blank registration form when registration page is first requested
#process completed registration forms, and log in new user
def register(request):
    """Register a new user"""
    if request.method != "POST":

        #GET request=instance of UserCreationForm w no data
        #display blank registration form
        form = UserCreationForm()

    else:
        #Process completed form
        #instance of UserCreationForm with submitted data
        form = UserCreationForm(data=request.POST)


        if form.is_valid():

        #save instance of form as new_user variable(Username & password)
            new_user = form.save()


            #Log the user in
            #call request but now with users data = logged in
            login(request, new_user)

            #redirct to home page after login
            return redirect("learning_logs:index")

    #display blank or invalid form
    context = {"form": form}
    return render(request, "registration/register.html", context)
