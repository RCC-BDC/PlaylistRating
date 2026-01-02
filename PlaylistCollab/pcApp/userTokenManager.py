from django.utils import timezone
from datetime import timedelta
from .models import SpotifyToken
import random
import string
from django.utils import timezone

# Only creates a user and saves state to verify in callback
def createUserTokenEntry(state):
    user = ''.join(random.choices(string.ascii_letters, k=16))
    entry = SpotifyToken(user=user, state=state)
    entry.save()
    print("User entry created")
    return user

def updateUserWithAccessToken(state, data):
    userEntry = SpotifyToken.objects.filter(state=state)[0]
    if userEntry:
        userEntry.expires_in = timezone.now() + timedelta(seconds=3600)
        userEntry.access_token = data.get("access_token")
        userEntry.token_type = data.get("token_type")
        userEntry.refresh_token = data.get("refreshToken")
        userEntry.save(update_fields=['access_token', 'token_type', 'expires_in', 'refresh_token'])
        print("Updated user entry")
    else:
        print("User Not Found. Cannot update token")
        return None

    return

def searchUser(userId):
    userEntry = SpotifyToken.objects.filter(user=userId)
    if userEntry.exists():
        return True
    else:
        print("User not found when retrieving")
        return False

def checkState(state):
    entry = SpotifyToken.objects.filter(state=state)
    if entry.exists():
        return True
    else:
        print("State Not Found")
        return False

def getUser(userId):
    entry = SpotifyToken.objects.filter(user=userId)[0]
    if entry == None:
        print("User Not Found")
        return False
    return entry


def isTokenExpired(userId):
    entry = getUser(userId)
    expiration_time = entry.expires_in
    current_time = timezone.now()
    if current_time < expiration_time:
        return False
    else:
        print("Token is expired")
        return True



