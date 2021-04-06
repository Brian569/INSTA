from django.shortcuts import render, redirect
from .models import Profile, Image, Follow, User, Comment
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required
def home(request):
    if request.method == 'GET':
        photos = Image.objects.all()

    context = {"photos": photos}

    return render(request, 'home.html', context)

@login_required

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request, prof_id):
	user=User.objects.get(pk=prof_id)
	images = Image.objects.filter(profile = prof_id)
	title = User.objects.get(pk = prof_id).username
	profile = Profile.objects.filter(user = prof_id)

	if Follow.objects.filter(user_from=request.user,user_to = user).exists():
		is_follow = True
	else:
		is_follow = False

	followers = Follow.objects.filter(user_to = user).count()
	following = Follow.objects.filter(user_from = user).count()
	

	return render(request,'my_accounts/profile.html',{"images":images,"profile":profile,"title":title,"is_follow":is_follow,"followers":followers,"following":following})
	

@login_required
def updateProfile(request):

	current_user = request.user

	if request.method == 'POST':
		if Profile.objects.filter(user_id = current_user).exists():
			form = UpdateProfile(request.POST,request.FILES,instance = Profile.objects.get(user_id = current_user))
		
		else:
			form = UpdateProfile(request.POST, request.FILES)

		if form.is_valid():
			user_profile = form.save(commit=False)
			user_profile.user = current_user
			user_profile.save()

			return redirect('profile', current_user.id)

	else:
		if Profile.objects.filter(user_id = current_user).exists():
			form = UpdateProfile(instance = Profile.objects.get(user_id = current_user))
		else:
			form = UpdateProfile()

	return render(request, 'my_accounts/update_profile.html', {"form": form})