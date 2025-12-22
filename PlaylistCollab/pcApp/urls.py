from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('alive', views.apicheck),
    path('test', views.getTrack),
    path('spotifyAuth', views.spotifyAuthoization.as_view()),
    path('redirect', views.spotifyCallBack),
    path('getTopArtists', views.getUserTopArtists),
    path('UserTopArtists', views.renderUserArtistPage)
]