from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('authorize', views.spotifyAuthoization.as_view()),
    path('redirect', views.spotifyCallBack)
]