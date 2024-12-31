from django.utils import timezone
from datetime import timedelta
from .models import SpotifyToken

def getEntry(userId):
    userEntry = SpotifyToken.objects.filter(user=userId)
    if userEntry.exists():
        return userEntry[0]
    else:
        return None


# Only creates a user and saves state to verify in callback
def createUserTokenEntry(state):
    user = "TestUser"
    userEntry = getEntry(user)
    if userEntry:
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

