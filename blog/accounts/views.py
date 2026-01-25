from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

from .forms import SignupForm
from django.contrib.auth.models import User # Model for where the user information is default stored
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
def signup(request):
    if request.method == 'GET':
        form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form})
    if request.method == 'POST':
        username = request.POST.get("username")
        # Username is the email address of the user, checking if it's the valid format
        try:
            validate_email(username)
        except ValidationError:
            return render(request, 'accounts/signup.html', {'form': SignupForm(), 'errors': 'Please enter a valid email address.'})
        password = request.POST.get("password")
        # Check password meets requirements: 
        try:
            validate_password(password)
        except ValidationError:
            return render(request, 'accounts/signup.html', {'form': SignupForm(), 'errors': 'Password does not meet the requirements. Please ensure the password has at least 8 characters, includes both letters and numbers, and contains at least one special character.'})
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        # Create the new users now
        form = SignupForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname)
            return redirect('/accounts/login')  # Redirect to login page after successful, only if, signup
        else:
            return render(request, 'accounts/signup.html', {'form': form, 'errors': 'An error occured or the form is not valid. Please correct any errors and try again.'})



def login(request):
    if request.method == "GET": # Render the page witht the form here
        from .forms import LoginForm
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    if request.method == "POST":
        from django.contrib.auth import authenticate
        username = request.POST.get("username")
        password = request.POST.get("password")
        client = authenticate(username=username, password=password)
        if not client is None:
            from django.contrib.auth import login
            login(request, client)
            return redirect('/')  # Redirect to home page after successful login
        else:
            from .forms import LoginForm
            context = {"form": LoginForm(), "error": "Login failed. Check your username and password and try again..."}
            return render(request, 'accounts/login.html', context)