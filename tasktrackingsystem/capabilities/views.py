from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from . import forms
from .models import Capabilities

def capabilities_add(request):
    if request.method == 'POST':
        form = forms.CapabilitiesForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['Username']
            if not Capabilities.objects.filter(Username=user).exists():
                form.save()
                success_message = f'Capabilities for username {user} successfully added!'
                return render(request, 'capabilities/add_capabilities.html', {'form': form, 'success_message': success_message})
            else:
                warning_message = f'Capabilities for username {user} already exist!'
                return render(request, 'capabilities/add_capabilities.html', {'form': form, 'warning_message': warning_message})
            # return redirect('leader:leader_login')
    else:
        form = forms.CapabilitiesForm()
    return render(request, 'capabilities/add_capabilities.html', {'form': form})
