from django import forms

class AddPost(forms.Form):
    title = forms.CharField(label='Title')
    body = forms.CharField(label='Body', widget=forms.Textarea)
    # author = forms.CharField(label='Author') This will not be in the form that is shown to the user because I will get the username / author from the request itself. Hopefully....
