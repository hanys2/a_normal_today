from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, SignupForm
from django.utils import timezone
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, 'diary\main.html', {})
def index(request):
    posts = Post.objects.all()
    return render(request, 'diary\index.html', {'post':posts})
def post(request):
    posts = Post.objects.all()
    return render(request, 'diary\content.html', {'post':posts})
def post_detail(request, pk) :
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'diary\content.html', {'post':posts})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid(): 
            post = form.save(commit = False) 
            post.author = request.user
            post.publised_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'diary\write.html', {'form':form})
def signup(request):
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.signup()
            return redirect('login')
    else:
        signup_form = SignupForm()
    
    context = {
        'signup_form' : signup_form,
    }
    return render(request,'diary/signup.html',context)
