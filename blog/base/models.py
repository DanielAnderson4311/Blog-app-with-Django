from django.db import models

# Create your models here.

# Model for the posts
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    body = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100) # I want this to be automatic to Username later
    # like_count = models.IntegerField(default=0)
    

# Model for the comments
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # CASCADE means that if the post gets deleted, so will the comments
    username = models.CharField(max_length=100) # Also want to be automatic to Username later, which will be done through request.user to get their user name and email.......
    body = models.TextField(max_length=1000)
    date_pub = models.DateTimeField(auto_now_add=True)
    # like_count = models.IntegerField(default=0)



# More models to come as needed

