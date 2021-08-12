from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post #tells Django which model to use with this form 
        fields = ('title','text') #tells Django which fields in model to update, user will be who is already logged in and created date will be automatically generated
