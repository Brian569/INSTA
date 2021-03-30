from django.shortcuts import render, redirect
from .models import Profile, Image

def home(request):
    if request.method == 'GET':
        photos = Image.objects.all()

    context = {"photos": photos}

    return render(request, 'home.html', context)

def my_profile(request):
    
    profile = request.GET.get('profile')
    if profile == None:
        photo = Image.objects.all()

    else:
        photo = Image.objects.filter(profile__name__contains=profile)

    profile = Profile.objects.all()

    context = {'profile': profile, 'photo': photo}
    prof_temps = {''}

    return render(request, 'profiles/profile.html',context)

def user_profile(request):

    return render(request, 'profiles/user_profile.html')

def edit_profile(request):

    return render(request, 'profiles/edit_profile.html')

def comments(request):

    profile = request.GET.get('comments')
    if profile == None:
        photo = Image.objects.all()
    
    else:
        photo = Image.objects.filter(profile__name__contains=comments)

    profile = Profile.objects.all()

    context = {'profiles': profile, "photos" : photo}

    return render(request, 'profiles/comments.html', context)