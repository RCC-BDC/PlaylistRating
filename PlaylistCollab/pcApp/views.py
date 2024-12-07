from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from .models import SpotifyToken
from .spotifyutils import updateSpotifyToken
import os
import requests
import base64
import json

# Create your views here.

def homePage(request):
    # Authorize Spotify

    return render(request, "index.html")


def testCall(request):
    # Create request

    # Need to source script for values
    client_id = os.environ['client_id']
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
    req = requests.post(url, data=body, headers=headers)

    data = req.json()
    print(data)
    updateSpotifyToken(data)

    return HttpResponse(status=200)



def getTrack(request):

    base_url = "https://api.spotify.com/v1/tracks/"
    track_id = "1dHJETCn2X1R1YwVlMvSza"
    full_url = base_url + track_id

    data = SpotifyToken.objects.filter(user="TestUser")
    token = data[0].access_token
    headers = {"Authorization": f"Bearer {token}" }

    req = requests.get(full_url, headers=headers)
    resp = req.json()
    print(resp)

    return HttpResponse(status=200)




