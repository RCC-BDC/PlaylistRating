from django.utils import timezone
from datetime import timedelta, datetime
from .models import SpotifyToken
from time import time
from requests import get

def getEntry(userId):
    userEntry = SpotifyToken.objects.filter(user=userId)
    if userEntry.exists():
        return userEntry[0]
    else:
        print("User not found when retrieving")
        return None


# Only creates a user and saves state to verify in callback
def createUserTokenEntry(state):
    user = "TestUser"
    userEntry = getEntry(user)
    if userEntry:
        print("User already exists, check if token expired")
        diff = userEntry.expires_in.timestamp() - time()
        if diff < 0:
            print("User token expired, update token")
            # Eventually get refresh logic
            userEntry.delete()
        else:
            print("User token is good")
            return None

    entry = SpotifyToken(user=user, state=state)
    entry.save()
    print("User entry created")
    return


def updateSpotifyToken(accessToken, tokenType, refreshToken):
    user = "TestUser"
    userEntry = getEntry(user)
    if userEntry:
        userEntry.expires_in = timezone.now() + timedelta(seconds=3600)
        userEntry.access_token = accessToken
        userEntry.token_type = tokenType
        userEntry.refresh_token = refreshToken
        userEntry.save(update_fields=['access_token', 'token_type', 'refresh_token', 'expires_in'])
        print("Updated user entry")
    else:
        print("User Not Found. Cannot update token")
        return None

    return


def getState():
    user = "TestUser"
    userEntry = getEntry(user)

    if userEntry:
        return userEntry.state

    else:
        print("User Not Found. Cannot retrieve state")
        return

def executeGetReq(endpoint):
    baseUrl = "https://api.spotify.com"
    url = baseUrl + endpoint
    print("Url= " + url)

    user = getEntry("TestUser")
    accessToken = user.access_token
    tokenType = user.token_type
    headers = {"Authorization": tokenType + " " + accessToken}

    res = get(url, headers=headers)
    print(res)
    print(res.json())

    return


