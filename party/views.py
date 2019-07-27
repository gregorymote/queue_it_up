import os
import sys
import json
import spotipy
import webbrowser
import time
import random
import spotipy.util_custom as util
from json.decoder import JSONDecodeError

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from party.forms import LoginForm
from party.forms import NamePartyForm
from party.forms import CreateUserForm
from party.forms import AuthForm
from game.forms import blankForm
from party.models import Party
from party.models import Users

secret='4ebf1b0ef7a34002bf95f8c2aa8365b0'
uri = 'http://localhost:8000/party/auth/'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'
cl_id='6de276d9e60548d5b05a7af92a5db3bb'

def login(request):
    
    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
           
            uname = form.cleaned_data['username']
        
            auth_code = getCode()
            p = Party(name='creating party', username=uname, code=auth_code)
            p.save()
            
            try:
                util.generateURL(uname, scope, client_id=cl_id, client_secret=secret, redirect_uri= uri)
            except (AttributeError, JSONDecodeError):
                os.remove(f".cache-{username}")
                util.generateURL(username, scope, client_id=cl_id ,client_secret=secret, redirect_uri= uri)

            return HttpResponseRedirect(reverse('your_code', kwargs={'pid':p.pk, 'code':auth_code}))
            
    else:
        form = LoginForm(initial= {'username' : ''})

    context = {
        'form' : form,
        }

    return render(request, 'party/login.html', context)

def your_code(request, pid, code):
    
    p = Party.objects.get(pk = pid)
    isVisible = False

    if p.url != None and p.token == None:
        print ('visited')
        try:
            p.token = util.createToken(p.url, p.username, scope, client_id=cl_id, client_secret=secret, redirect_uri= uri)
            p.save()
        except (AttributeError, JSONDecodeError):
            os.remove(f".cache-{username}")
            p.token = util.createToken(p.url, p.username, scope, client_id=cl_id ,client_secret=secret, redirect_uri= uri)
            p.save()
        isVisible = True
        print('token created')

    if request.method == 'POST':
        form = blankForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect(reverse('start_party', kwargs={'pid':p.pk,}))

    else:
        form = blankForm(initial ={'blank':''})

    context = {
               'form':form,
               'code':code,
               'isVisible': isVisible,
               }
    return render(request, 'party/your_code.html', context)


def choose_device(request, pid):
    
    p = Party.objects.get(pk = pid)
    spotifyObject = spotipy.Spotify(auth=p.token)
            
    return render(request, 'party/choose_device.html')



def auth(request):

    url = getURL(str(request.get_full_path))

    if request.method == 'POST':

        form = AuthForm(request.POST)

        if form.is_valid():
            auth_code = form.cleaned_data['auth_code']
            try:
                p = Party.objects.get(code=auth_code)
                p.url = url
                p.save()
                return HttpResponseRedirect(reverse('complete'))
            except:
                print("could not find party with auth code: " + auth_code)
    else:
        form = AuthForm(initial={'auth_code':''})
    
    context = {'form': form,}
    
    return render(request, 'party/auth.html', context)


def complete(request):

    return render(request, 'party/complete.html')

def name_party(request, pid):

    p = Party.objects.get(pk = pid)

    if request.method == 'POST':

        form = NamePartyForm(request.POST)

        if form.is_valid():
            p.name=form.cleaned_data['party_name']
            p.roundNum = 1
            p.roundTotal = 1
            p.started = False
            p.state = 'assign'
                      
            p.save()          
            
            u = Users(
                name = form.cleaned_data['user_name'],
                party = p,
                sessionID = request.session.session_key,
                points = 0,
                isHost = True,
                hasSkip = True,
                hasPicked = False,
                turn = "not_picked",
                )
            u.save()
                
            return HttpResponseRedirect(reverse('lobby', kwargs={'pid':p.pk}))
        
    else:

            
        form = NamePartyForm(initial={
                                    'party_name' : 'Enter a Party Name',
                                    'user_name' : 'name'})


    context = {
        'form' : form,
        }

    return render(request, 'party/name_party.html', context)

def create_user(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():

            #print('\n\n\n\n',request.session.session_key,'\n\n\n\n\n')
            u = Users(
                    name= form.cleaned_data['user_name'],
                    party = form.cleaned_data['party_choice'],
                    sessionID = request.session.session_key,
                    points = 0,
                    isHost = False,
                    hasSkip = True,
                    hasPicked = False,
                    turn = "not_picked",
                    )
            u.save()

            

            return HttpResponseRedirect(reverse('lobby', kwargs={'pid':u.party.pk}))
    else:
        form = CreateUserForm(initial={
                                        'party_choice': '',
                                        'user_name': 'name'})

    context = {
        'form' : form,
        }

    return render(request, 'party/create_user.html', context)

def getCode():
    code = ""                                    
    for x in range(5):
        code = chr(random.randint(41,123)) + code
    return code
                                            
def getURL(path):

    i = 0
    while path[i] != '/':
        i = i + 1
    start = i

    while path[i] != '\'':
        i = i + 1
    end = i

    url = 'localhost:8000' + path[start:end]

    return url
                                         
                                           
