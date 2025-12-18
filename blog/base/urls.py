from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), # Render home page at root
    path('home/', views.home), # Render home page
    path('dashboard/', views.dashboard), # Render dashboard page    
    path('create/', views.create),
    path('posts/', views.viewall), # This will be for the page with all the posts (sorted by date) in the WHOLE SITE
    path('viewpost/', views.viewpost),
]
