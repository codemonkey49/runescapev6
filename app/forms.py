from django.forms import ModelForm
from django.forms.widgets import *
from models import componentModel,tutorialModel
 
class componentForm(ModelForm):
    class Meta:
        model = componentModel
        fields = ['componentType', 'componentContent', 'image','imageCaption',"order"]
        widgets = { 'componentContent': Textarea(attrs={'size': 80})}
        
class tutorialForm(ModelForm):
    class Meta:
        model=tutorialModel
        fields=["title"]