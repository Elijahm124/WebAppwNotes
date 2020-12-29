#form = page that lets user input info
#we must validate and store info
from django import forms

#Topic is first model we work with, same directory
#aslo work with Entry model, allow us to submit data as entry
from .models import Topic, Entry

#ModelForm class uses info from models to create a form
class TopicForm(forms.ModelForm):

    # Meta tells django which model to build form
    # AND what fields to have in form
    class Meta:

        #build form from Topic model
        model = Topic

        #we include the text as a field (not date_added)
        # we dont include a label for the field
        fields = ['text']
        labels = {"text": ""}


class EntryForm(forms.ModelForm):
    class Meta:

        #build form from Entry model
        model = Entry

        #user can submit text, (not date added)
        fields = ["text"]

        #text field is not labeled
        labels = {"text": ""}

        #widget is HTML form element, (text box, list, etc.)
        #this line overrides default widget attributes
        #text area will be 80 columns wide(usual is 40)
        widgets = {"text": forms.Textarea(attrs={"cols":80})}