from django.shortcuts import render


# Create your views here.

def home(request): # Renders home page
    return render(request, 'base/index.html')
def dashboard(request): # Renders dashboard page
    return render(request, 'base/dashboard.html')
def viewpost(request): # renders view post page
    return render(request, 'base/view-post.html')