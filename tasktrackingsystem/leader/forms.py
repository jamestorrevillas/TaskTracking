from django import forms
from .models import Leader
from user.models import User
from project.models import Project

class LeaderForm(forms.ModelForm):
    Username = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=True,
        empty_label="Select",
    )
    Project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        required=True,
        empty_label="Select",
    )
    class Meta:
        model = Leader
        fields = ['Username', 'Project']
