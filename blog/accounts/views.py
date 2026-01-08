from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.

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
            return redirect('accounts/login.html')  # Redirect to login page after successful, only if, signup
        else:
            return render(request, 'accounts/signup.html', {'form': form, 'errors': 'An error occured or the form is not valid. Please correct any errors and try again.'})



def login(request):
    pass