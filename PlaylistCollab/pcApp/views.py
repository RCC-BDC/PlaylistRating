from django.shortcuts import render

# Create your views here.

def homePage(request):
    # Authorize Spotify

    return render(request, "index.html")
