from django import forms

class AddPost(forms.Form):
    title = forms.CharField(label='Title')
    body = forms.CharField(label='Body', widget=forms.Textarea)
    author = forms.CharField(label='Author')
