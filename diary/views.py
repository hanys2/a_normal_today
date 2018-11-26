from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    return render(request, 'diary\main.html', {})
def index(request):
    posts = Post.objects.all()
    return render(request, 'diary\index.html', {'post':posts})
def post(request):
    posts = Post.objects.all()
    return render(request, 'diary\content.html', {'post':posts})
def registration(request):
    posts = Post.objects.all()
    return render(request, 'registration\register.html', {'post':posts})

