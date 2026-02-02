from django.shortcuts import render


# Create your views here.

def home(request): # Renders home page
    return render(request, 'base/index.html')
def dashboard(request): # Renders dashboard page
    return render(request, 'base/dashboard.html')
def viewpost(request): # renders view post page
    return render(request, 'base/view-post.html')


# Dealing with a creating post
from .forms import AddPost
from .models import Post



def create(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            # I am going to make this deal with the request
            form = AddPost(request.POST) # Added data: author (to be automatic), title, body
            if form.is_valid():
                title = form.cleaned_data['title']
                body = form.cleaned_data["body"]

                creator = request.user.username  # Get the username of the user that is in the logged int request currently
                from django.contrib.auth.models import User
                # The author will be the user's email (backup if creator not works)
                author = request.user.username # The usrename is the email
                creator = request.user  # Get the user object i tself for the fforeignkey field
                # Save it
                new_post = Post(title=title, body=body, author=author, creator=creator) # The rest is added when it is sent to the db
                new_post.save()
                return render(request, 'base/add-post.html', {'form': AddPost(), 'success': True})
        else:
            return render(request, 'base/add-post.html', {'form': AddPost(), 'errors': 'You must be logged in to create a post.'})
    else:
        form = AddPost()
        return render(request, 'base/add-post.html', {'form': form})



from .models import Post
def viewall(request):
    posts = Post.objects.all().order_by('-date_pub') # Newest first
    content = {
        "posts": posts 
    }
    return render(request, 'base/viewall.html', content)




def myposts(request):
    pass