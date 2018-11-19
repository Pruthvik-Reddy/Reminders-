from django import forms

class reminderform(forms.Form):
    name=forms.CharField(max_length=100)
    #date=forms.DateTimeField()
    time=forms.TimeField()
    description=forms.CharField(widget=forms.Textarea)