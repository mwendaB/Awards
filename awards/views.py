from django.shortcuts import render
from .models import Projects,Profile
from .forms import profileForm,UserUpdateForm,RegistrationForm,projectForm,UpdateUserProfileForm,RateForm
# Create your views here.

def index(request):
    projects = Projects.objects.all()
    return render(request,'index.html',{"projects":projects})


def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        procForm=profileForm(request.POST, request.FILES)
        if form.is_valid() and procForm.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            profile=procForm.save(commit=False)
            profile.user=user
            profile.save()


        return redirect('login')
    else:
        form= RegistrationForm()
        prof=profileForm()
    params={
        'form':form,
        'profForm': prof
    }
    return render(request, 'users/register.html', params)


