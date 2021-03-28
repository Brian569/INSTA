from django.shortcuts import render
from .models import Profile, Image


def home(request):

    return render(request, 'home.html')

def my_profile(request):
    
    profile = request.GET.get('profile')
    if profile == None:
        photo = Image.objects.all()

    else:
        photo = Image.objects.filter(profile__name__contains=profile)

    profile = Profile.objects.all()

    context = {'profile': profile, 'photo': photo}

    return render(request, 'profiles/profile.html',context)

def user_profile(request):

    return render(request, 'profiles/user_profile.html')

def edit_profile(request):

    return render(request, 'profiles/edit_profile.html')