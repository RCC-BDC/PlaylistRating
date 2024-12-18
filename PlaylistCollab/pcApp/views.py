from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from .models import SpotifyToken
from .spotifyutils import updateSpotifyToken
from requests import Request, post, get
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import os
import base64
import string
import random
import json

# Create your views here.

def homePage(request):

    # Authorize Spotify
    return render(request, "index.html")

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
        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'client_id': client_id,
            'response_type': response_type,
            'redirect_uri': redirect,
            'state': state,
            'scope': scopes
        }).prepare().url

        return Response({'url': url}, status=status.HTTP_200_OK)


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
    req = post(url, data=body, headers=headers)

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

    req = get(full_url, headers=headers)
    resp = req.json()
    print(resp)

    return HttpResponse(status=200)


