from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from . import forms
from .models import Leader

def leader_add(request):
    if request.method == 'POST':
        form = forms.LeaderForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['Username']
            if not Leader.objects.filter(Username=user).exists():
                form.save()
                success_message = f'Username {user} successfully added as a leader!';
                return render(request, 'leader/add_leader.html', {'form': form, 'success_message': success_message})
            else:
                warning_message = f'Username {user} is already a leader!';
                return render(request, 'leader/add_leader.html', {'form': form, 'warning_message': warning_message})
            #return redirect('leader:leader_login')
    else:
        form = forms.LeaderForm()
    return render(request, 'leader/add_leader.html', {'form': form})
