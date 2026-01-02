from .models import SpotifyToken
from requests import get
from .dataParser import parsePlaylistReturn
import os
from requests import Request, post
from django.http import HttpResponse
import base64

def buildSpotifyAuthUrl(user, state):
    # Prepare url for client to get spotify permission
    scopes = 'user-top-read'
    client_id = os.environ['client_id']
    response_type = 'code'
    redirect = os.environ['redirect_url']

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

    resp = HttpResponse(url)
    resp.set_cookie("usr", user)
    resp.status_code = 200

    return resp

def getAccessTokenFromSpotify(code):
    # Gather data to request access token from spotify
    client_id = os.environ['client_id']
    secret_id = os.environ['secret_id']
    redirectUrl = os.environ['redirect_url']
    token_str = client_id + ":" + secret_id
    token_ascii_bytes = token_str.encode('ascii')
    base_64_enc = base64.b64encode(token_ascii_bytes)
    base_64_str = base_64_enc.decode('ascii')

    # Request access token from spotify
    # Need to pass code from spotify back to spotify authorization to retrieve the auth token
    url = 'https://accounts.spotify.com/api/token'
    data = {'grant_type': 'authorization_code', 'code': code, 'redirect_uri': redirectUrl}
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": f"Basic {base_64_str}"}
    print("Sending Post request to spotify")
    res = post(url, data=data, headers=headers)
    print("Parsing response into json")
    responseData = res.json()

    return responseData


def getState(user):
    print(user)
    userEntry = getEntry(user)
    if userEntry:
        return userEntry.state
    else:
        print("User Not Found. Cannot retrieve state")
        return

def executeGetReq(userObj, endpoint):
    baseUrl = "https://api.spotify.com"
    url = baseUrl + endpoint
    print("Url= " + url)

    accessToken = userObj.access_token
    tokenType = userObj.token_type
    headers = {"Authorization": tokenType + " " + accessToken}

    res = get(url, headers=headers)
    return res

def getPlaylist(playlistId):
    base_url = "https://api.spotify.com/v1/playlists/"
    #playlist_id = "7mUiJ5dq241vFALzw7FKSb/tracks?limit=2&fields=items(added_at,added_by.id,track(name,artists(name),album(name)))"
    #full_url = base_url + playlistId + "/tracks?limit=2&fields=items(added_at,added_by.id,track(name,artists(name),album(name)))"

    limiter = "/tracks?fields=items(added_at, added_by.id, track(name,artists(name),album(name))"
    full_url = base_url + playlistId

    data = SpotifyToken.objects.filter(user="TestUser")
    token = data[0].access_token
    headers = {"Authorization": f"Bearer {token}" }

    req = get(full_url, headers=headers)
    resp = req.json()
    #print(resp)
    print(full_url)

    parsed_data = parsePlaylistReturn(resp)

    #print(parsed_data)


