from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Projects,Profile,Review,RATE_CHOICES



class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'photo', 'bio']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'photo']     
        
