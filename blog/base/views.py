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
        # I am going to make this deal with the request
        form = AddPost(request.POST) # Added data: author (to be automatic), title, body
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data["body"]
            author = form.cleaned_data["author"]
            # Save it
            new_post = Post(title=title, body=body, author=author)
            new_post.save()
            return render(request, 'base/add-post.html', {'form': AddPost(), 'success': True})
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