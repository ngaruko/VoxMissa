from django.shortcuts import render

# Create your views here.
import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.test import TestCase

from users.models import Profile
from .models import Event, Submission
from .forms import SubmissionForm, CustomUserCreateForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from PIL import Image
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
# Create your views here.


import time
from datetime import datetime


def events(request):
    events = Event.objects.all()
    context = { 'events':events}
    return render(request, 'events.html', context)

def event(request, pk):
    event = Event.objects.get(id=pk)
    
    registered = False
    submitted = False
    
    if request.user.is_authenticated:
        print(request.user)
        profile = Profile.objects.get(user=request.user)
        registered = profile.events.filter(id=event.id).exists()
        submitted = Submission.objects.filter(participant=profile, event=event).exists()
    context = {'event':event, 'registered':registered, 'submitted':submitted}
    return render(request, 'event.html', context)


@login_required(login_url='/login')
def registration_confirmation(request, pk):
    event = Event.objects.get(id=pk)

    if request.method == 'POST':
        event.participants.add(Profile.objects.get(user=request.user))
        return redirect('event', pk=event.id)

    
    return render(request, 'event_confirmation.html', {'event':event})

@login_required(login_url='/login')
def registration_confirmation(request, pk):
    event = Event.objects.get(id=pk)

    if request.method == 'POST':
        event.participants.add(Profile.objects.get(user=request.user))
        return redirect('event', pk=event.id)

    
    return render(request, 'event_confirmation.html', {'event':event})

@login_required(login_url='/login')
def proposal_submission(request, pk):
    event = Event.objects.get(id=pk)

    form = SubmissionForm()

    if request.method == 'POST':
        form = SubmissionForm(request.POST)

        if form.is_valid():
            submission = form.save(commit=False)
            submission.participant = Profile.objects.get(user=request.user)
            submission.event = event
            submission.save()
            
            return redirect('account')

    context = {'event':event, 'form':form}
    return render(request, 'submit_form.html', context)


#Add owner authentication
@login_required(login_url='/login')
def update_submission(request, pk):
    submission = Submission.objects.get(id=pk)
    profile = Profile.objects.get(user=request.user)

    if profile != submission.participant:
        return HttpResponse('You cant be here!!!!')

    event = submission.event
    form = SubmissionForm(instance=submission)

    if request.method == 'POST':
        form = SubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('account')


    context = {'form':form, 'event':event}

    return render(request, 'submit_form.html', context)
