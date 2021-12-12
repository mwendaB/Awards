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


class projectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title','description','shot','link']  

        
class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:

            user.save()
        return user  

    
class RateForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['text','design','usability','content']          
           
    
        
