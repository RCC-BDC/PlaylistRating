from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('alive', views.apicheck),
    path('createacct', views.createAccountReq),
    path('login', views.loginReq),
    path('test', views.getTrack),
    path('newUserAcct', views.createUserAccount),
    path('updateSpotifyAccess', views.clientCredCall),
    path('getPlaylist', views.getPlaylist),
    path('playlistLink', views.getPlaylistLink)
]