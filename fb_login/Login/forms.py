from django.forms import ModelForm
from Login.models import Create
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class createForm(ModelForm):
    class Meta:
        model=Create
        fields="__all__"
class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']
class resumeViewForm(ModelForm):
    class Meta:
        model=Create
        fields="__all__"
class resumeEditForm(ModelForm):
    class Meta:
        model=Create
        fields="__all__"
class resumeDeleteForm(ModelForm):
    class Meta:
        model=Create
        fields="__all__"
class resumepublicForm(ModelForm):
    class Meta:
        model=Create
        fields="__all__"
