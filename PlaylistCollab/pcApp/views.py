from django.shortcuts import render
from django.http import JsonResponse
from .spotifyUtils import *
from .userTokenManager import *
from .dataParser import *
from .requestHandler import *
from requests import post, get
from rest_framework.decorators import api_view
import os
import base64
import string
import random
from django.views.decorators.csrf import requires_csrf_token, csrf_protect


# Create your views here.

def homePage(request):
    return render(request, "index.html")

def createAccountReq(request):
    return render(request, "create_account.html")

def renderUserArtistPage(request):
    return render(request, "artists_page.html")

def renderUserSongPage(requst):
    return render(requst, "songs_page.html")

# Deprecated function
@csrf_protect
def createUserAccount(request):
    print("createUserAcct - views")
    res = None
    if res:
        return HttpResponse(status=201)
    return HttpResponse(reason="Username Taken", status=400)

@api_view(['GET'])
def spotifyAuthoization(request):
    # See if they already were logged in
    currentUserId = request.COOKIES.get("usr")

    # if true, look for user in database
    if currentUserId:
        userExists = searchUser(currentUserId)
        if userExists:
            # See if spotify token has expired
            expired = isTokenExpired(currentUserId)
            if not expired:
                data = "Found"
                resp = HttpResponse(data, status=200)
                return resp

    # else create a user entry in db and give them a token
    state = ''.join(random.choices(string.ascii_letters, k=16))
    user = createUserTokenEntry(state)

    resp = buildSpotifyAuthUrl(user, state)
    return resp

def spotifyCallBack(request, format=None):
    print("Received spotify callback")

    # Get data from request
    code = request.GET['code']
    state = request.GET['state']

    # Check that states align
    # Check state
    if not checkState(state):
        print("States do match")
        resp = HttpResponse("Issue Authorizing")
        resp.status_code = 500
        return resp

    resp = getAccessTokenFromSpotify(code)

    # Update db with access token
    updateUserWithAccessToken(state, resp)

    # Redirect to metrics page
    data = "Found"
    responseToClient = HttpResponse(data, status=200)
    return redirect("/UserTopArtists")


@api_view(['GET'])
def apicheck(request):
    print("Alive")
    return HttpResponse(status=200)

@api_view(['GET'])
def testCall(request):
    endpoint = "/v1/me"
    executeGetReq(endpoint)
    return HttpResponse(status=200)

@api_view(['GET'])
def getUserTopArtists(request):
    print("Top Artist View")
    # See if user is authenticated
    currentUserId = request.COOKIES.get('usr')
    if currentUserId == None:
        return HttpResponse(status=403)

    # use user cookie to find session, check for entry and expires_in
    userObject = getUser(currentUserId)
    expired = isTokenExpired(userObject.user)
    if expired:
        # Redirect user to homepage
        data = "Expired"
        resp = HttpResponse(data, status=200)
        return resp

    # Make call to spotify to get user data
    endpoint = "/v1/me/top/artists?limit=10"
    response = executeGetReq(userObject, endpoint)

    # Parse data into form readable for client
    parsedArtists = parseTopArtists(response.json())
    resp = {"artists": parsedArtists}

    # Return data to client
    return JsonResponse(resp, status=200)


@api_view(['GET'])
def getUserTopSongs(request):
    # See if user is authenticated
    currentUserId = request.COOKIES.get('usr')
    if currentUserId == None:
        return HttpResponse(status=403)

    # use user cookie to find session, check for entry and expires_in
    userObject = getUser(currentUserId)
    expired = isTokenExpired(userObject.user)
    if expired:
        # Redirect user to homepage
        data = "Expired"
        resp = HttpResponse(data, status=200)
        return resp

    # Make call to spotify to get user data
    endpoint = "/v1/me/top/tracks?limit=10"
    response = executeGetReq(userObject, endpoint)

    # Parse data into form readable for client
    parsedTracks = parseTopTracks(response.json())
    resp = {"tracks": parsedTracks}

    # Return data to client
    return JsonResponse(resp, status=200)

def getPlaylistWeb(request):
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
    print("Get PLaylist Endpoint")
    link = request.POST.get("link")
    playlist_id = parseLink(link)
    getPlaylist(playlist_id)

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

# Currently used for just client_credentials token
# Deprecated
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
    updateUserWithAccessToken(data)

    return HttpResponse(status=200)




