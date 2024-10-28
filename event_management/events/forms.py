from django import forms
from .models import Event
from .models import Location
from .models import Comment

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'start_date', 'end_date']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['title', 'due_date']  # Укажите поля, которые хотите использовать в форме
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']