from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home), # Render home page
    path('dashboard/', views.dashboard), # Render dashboard page    
    path('viewpost/', views.viewpost),
]
