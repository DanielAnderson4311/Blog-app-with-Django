from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), # Render home page at root
    path('home/', views.home), # Render home page
    # Render dashboard page is in the accounts app now 
    path('create/', views.create),
    path('posts/', views.viewall), # This will be for the page with all the posts (sorted by date) in the WHOLE SITE
    path('viewpost/', views.viewpost),
    path('posts/myposts/', views.myposts), # This will be for the page with the posts that the user has created. It will be found by searching the DB in the author field for the same user that created it
    path('posts/myposts/edit/<int:post_id>/', views.editpost), # this will be for the page to edit a post. I WILL need to check that the user has the permission to edi this post by comparing the user and the publisher
]
