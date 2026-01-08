from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder':'Enter your email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}), label='')
    fname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'First name'}),
        max_length=50,
        label=''
    )
    lname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Last name'}), label='')

class LoginForm(forms.Form):
    username = forms.Charfield(max_length=150, widget=forms.TextInput(attrs={'placeholder':'Enter your email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}), label='')