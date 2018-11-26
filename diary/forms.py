from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta: #상속
        model = Post
        fields = ('title','text',)
