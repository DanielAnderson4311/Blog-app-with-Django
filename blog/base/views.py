from django.shortcuts import render


# Create your views here.

def home(request): # Renders home page
    return render(request, 'base/index.html')
def dashboard(request): # Renders dashboard page
    return render(request, 'base/dashboard.html')
def viewpost(request, post_id): # renders view post page
    from .models import Post
    from django.core.exceptions import ObjectDoesNotExist
    # Check if the item is in the model first
    try:
        item = Post.objects.get(id=post_id)
    except ObjectDoesNotExist:
        return render(request, 'base/index.html')
    # Object exists if this point is reached, now to show the page:
    content = {"post": item}
    return render(request, 'base/view-post.html', content)


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
    from .models import Post
    # Get the user's username
    user = request.user.username
    posts = Post.objects.filter(author=user).order_by('-date_pub') # Get the posts that the user created, newest first
    # Mkae it accessbible to the HTML page and render
    content = {"posts": posts}
    return render(request, 'base/myposts.html', content)



def editpost(request, post_id):
    from .models import Post
    thepost = post_id # This will set thepost to the ID that i want to edit
    user = request.user
    post = Post.objects.get(id=thepost)
    #CEHECK IT MATCHES
    if not request.user.is_authenticated: # First check that they are logged in
        from django.shortcuts import redirect
        return redirect('/')
    else:
        pass
    if post.creator != user: # Now check that they are the user that created it
        # It doesn't not match
        from django.shortcuts import redirect
        return redirect('/')
    else:
        # CORRECT
        if request.method == "GET":
            details = Post.objects.get(id=thepost)
            from .forms import AddPost
            edit_form = AddPost(initial={
                "title": details.title,
                "body": details.body,
            }) # Fill form witht he details that I pull fromt eh database further up
            return render(request, 'base/edit_post.html', {'form': edit_form, "post_id": post_id})
        if request.method == "POST":
            from .forms import AddPost
            form = AddPost(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                body = form.cleaned_data['body']
                post.title = title
                post.body = body
                post.save() # Save the changes, UPDATE ENTRY RATHEr THAN CREATING A NEW ENTRY
                from django.shortcuts import redirect
                return redirect('/posts/myposts/') # Go back after editted

def deletepost(request, post_id):
    from .models import Post
    # CHECK THE PERSON HAS PERMISSION TO DELETE
    if not request.user.is_authenticated:
        from django.shortcuts import redirect
        return redirect('/')
    else:
        pass
    # Check that the user is the creator
    creator = Post.objects.get(id=post_id).creator
    if creator != request.user:
        from django.shortcuts import redirect
        return redirect('/')
    else:
        pass
    # PERMISSION GRANTED
    thepost = Post.objects.get(id=post_id)
    thepost.delete()
    from django.shortcuts import redirect
    return redirect('/posts/myposts/')



def search(request):
    # I want them to be able to search their own posts separately
    from .forms import SearchForm
    from .models import Post
    from django.db.models import Q

    if request.method == "POST":
        # Get the raw query from the HTML input
        form = SearchForm(request.POST)
        query = None
        if form.is_valid():
            query = form.cleaned_data["query"]
            query = query.strip()
        else:
            query = None
        # If the user typed something search.... (I will change the content dict to include all the different types of search result later. )
        if query:
            dataset = Post.objects.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query)
            ).order_by('-date_pub')

            content = {
                "posts": dataset,
                "form": SearchForm()
            }
            return render(request, 'base/search.html', content)
        # If query is empty, return no results
        return render(request, 'base/search.html', {
            "posts": Post.objects.none(),
            "form": SearchForm()
        })
    # GET request so show empty search page
    return render(request, 'base/search.html', {
        "posts": Post.objects.none(),
        "form": SearchForm()
    })
