from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User Registered Successfully')
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to Register user')
            return render(request, 'accounts/register.html', {'form':form})
    context = {
        'form': UserCreationForm
    }
    return render(request, 'accounts/register.html', context)