from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
from django.db import models

class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()
	phone_no=forms.CharField(max_length=10)
	class Meta:
		model=User
		fields=['username','email','phone_no','password1','password2',]
class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()
	phone_no=forms.CharField(max_length=10)
	class Meta:
		model=User
		fields=['username','email','phone_no']
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['image']
		