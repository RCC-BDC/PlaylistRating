from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.template import loader
from datetime import timedelta
from .models import SpotifyToken
from .spotifyutils import *
from .accountutils import *
from requests import Request, post, get
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import os
import base64
import string
import random
import json
from django.views.decorators.csrf import requires_csrf_token, csrf_protect


# Create your views here.

def homePage(request):

    # Authorize Spotify
    return render(request, "index.html")

def createAccountReq(request):
    return render(request, "create_account.html")

""""
class createUserAccount(APIView):
    @csrf_protect
    def post(self, request, format=None):
        print("User Account Created")
        return Response({}, status=status.HTTP_201_CREATED)
"""
@csrf_protect
def createUserAccount(request):
    print("createUserAcct - views")
    res = createUser(request.POST)
    if res:
        return HttpResponse(status=201)
    return HttpResponse(reason="Username Taken", status=400)

def loginReq(request):
    return render(request, "login.html")

class spotifyAuthoization(APIView):
    def get(self, request, format=None):
        scopes = 'playlist-read-collaborative'
        client_id = os.environ['client_id']
        response_type = 'code'
        # move redirect to script
        redirect = os.environ['redirect_url']
        state = ''.join(random.choices(string.ascii_letters, k=16))

        # Prepare url to send to spotify
        # Spotify then asks user to approve permissions then redirects to specified url
        print("Preparing url")
        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'client_id': client_id,
            'response_type': response_type,
            'redirect_uri': redirect,
            'state': state,
            'scope': scopes,
            'show_dialog': True
        }).prepare().url

        print("Creating user entry")
        createUserTokenEntry(state)
        return Response({'url': url}, status=status.HTTP_200_OK)


def spotifyCallBack(request, format=None):
    print("Received spotify callback")
    client_id = os.environ['client_id']
    secret_id = os.environ['secret_id']
    savedState = getState()

    token_str = client_id + ":" + secret_id
    token_ascii_bytes = token_str.encode('ascii')
    base_64_enc = base64.b64encode(token_ascii_bytes)
    base_64_str = base_64_enc.decode('ascii')

    code = request.GET['code']
    state = request.GET['state']

    if savedState != state:
        print("States are not equal")
        return

    redirectUrl = os.environ['redirect_url']
    url = 'https://accounts.spotify.com/api/token'
    data = {'grant_type': 'authorization_code', 'code': code, 'redirect_uri': redirectUrl}
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": f"Basic {base_64_str}"}

    print("Sending Post request to spotyify")
    res = post(url, data=data, headers=headers)

    print("Parsing response into json")
    responseData = res.json()
    access_token = responseData.get('access_token')
    token_type = responseData.get('token_type')
    refresh_token = responseData.get('refresh_token')
    endpoint = "/v1/me"
    executeGetReq(endpoint)
    print("Updating user entry")
    updateSpotifyToken(access_token, token_type, refresh_token)

    # need to save user token
    # render page
    return redirect("http://localhost:8000")


def testCall(request):
    endpoint = "/v1/me"
    executeGetReq(endpoint)
    return HttpResponse(status=200)


# Currently used for just client_credentials token
def clientCredCall(request):
    # Create request

    # Need to source script for values
    client_id = os.environ['client_id']
    print(client_id)
    secret_id = os.environ['secret_id']

    grant_type = "client_credentials"
    token_str = client_id + ":" + secret_id
    token_ascii_bytes = token_str.encode('ascii')
    base_64_enc = base64.b64encode(token_ascii_bytes)
    base_64_str = base_64_enc.decode('ascii')
    url = 'https://accounts.spotify.com/api/token'
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": f"Basic {base_64_str}"}
    body = {"grant_type": grant_type}

    # Send request
    req = post(url, data=body, headers=headers)

    data = req.json()
    print(data)
    updateSpotifyToken(data)

    return HttpResponse(status=200)

def getPlaylist(request):
    base_url = "https://api.spotify.com/v1/playlists/"
    playlist_id = "7mUiJ5dq241vFALzw7FKSb/tracks?limit=2"
    full_url = base_url + playlist_id

    data = SpotifyToken.objects.filter(user="TestUser")
    token = data[0].access_token
    headers = {"Authorization": f"Bearer {token}" }

    req = get(full_url, headers=headers)
    resp = req.json()
    print(resp)

    return HttpResponse(status=200)

def getPlaylistLink(request):
    print("Endpoint running")
    return HttpResponse(status=200)


def getTrack(request):
    base_url = "https://api.spotify.com/v1/tracks/"
    track_id = "1dHJETCn2X1R1YwVlMvSza"
    full_url = base_url + track_id

    data = SpotifyToken.objects.filter(user="TestUser")
    token = data[0].access_token
    headers = {"Authorization": f"Bearer {token}" }

    req = get(full_url, headers=headers)
    resp = req.json()
    print(resp)

    return HttpResponse(status=200)

def apicheck(request):
    print("Alive")
    return HttpResponse(status=200)


