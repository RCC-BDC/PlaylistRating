from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('alive', views.apicheck),
    path('createacct', views.createAccountReq),
    path('login', views.loginReq),
    path('authorize', views.spotifyAuthoization.as_view()),
    path('redirect', views.spotifyCallBack),
    path('test', views.testCall),
    path('newUserAcct', views.createUserAccount)
]