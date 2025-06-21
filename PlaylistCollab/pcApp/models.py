from django.db import models

# Create your models here.
class UserAccount(models.Model):
    Username = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=100)
    Created_at = models.DateTimeField(auto_now_add=True)
    Email = models.EmailField(max_length=100, blank=True, null=True)
    Token = models.CharField(max_length=64, unique=True)


class SpotifyToken(models.Model):
    user = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    refresh_token = models.CharField(max_length=150, null=True, blank=True)
    access_token = models.CharField(max_length=150, null=True, blank=True)
    expires_in = models.DateTimeField(null=True, blank=True)
    token_type = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=150, null=True, blank=True)

