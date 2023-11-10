from django import forms
from .models import Capabilities
from user.models import User


class CapabilitiesForm(forms.ModelForm):
    Username = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=True,
        empty_label="Select username",
    )

    class Meta:
        model = Capabilities
        fields = ['Username', 'Skills', 'Achievements']

        widgets = {
            'Skills': forms.Textarea(attrs={'placeholder': 'Type your skills here...'}),
            'Achievements': forms.Textarea(attrs={'placeholder': 'Type your achievements here...'}),
        }


class CapabilitiesLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Username', 'Password']
