from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home-page'),
    path('alive', views.apicheck),
    path('test', views.testCall),
    path('spotifyAuth', views.spotifyAuthoization),
    path('redirect', views.spotifyCallBack),
    path('getTopArtists', views.getUserTopArtists),
    path('UserTopArtists', views.renderUserArtistPage, name='user-artist-page')
]