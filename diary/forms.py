from django import forms
from .models import Post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.forms.widgets import PasswordInput, TextInput

User = get_user_model()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text','song','singer','link','image')


class SignupForm(forms.Form):

    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : "ID",
                }
        )
    )

    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : "PASSWORD",                
                }
        )
    )

    verify_password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : "PASSWORD CHECK",
                }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('아이디가 이미 사용중입니다.')
        return username

    def clean_verify_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('verify_password')
        
        if password1 != password2:
            raise forms.ValidationError('Password does not match')
        return password2

    def signup(self):
        if self.is_valid():
            return User.objects.create_user(
                username = self.cleaned_data['username'],
                password = self.cleaned_data['verify_password']
            )
