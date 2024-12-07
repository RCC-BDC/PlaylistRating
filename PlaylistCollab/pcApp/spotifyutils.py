from django.utils import timezone
from datetime import timedelta
from .models import SpotifyToken


def updateSpotifyToken(data):
    user = "TestUser"
    access_token = ""
    token_type = "Bearer"
    expires_in = timezone.now() + timedelta(seconds=3600)

    entry = SpotifyToken(user=user, access_token=access_token, token_type=token_type, expires_in=expires_in)
    entry.save()