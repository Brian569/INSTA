from django.shortcuts import render, redirect
from .models import Profile, Image, Follow, User, Comment
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required
def home(request):
	'''
	Method that fetches all images from all users.
	'''
	images = Image.objects.all()
	title = "Discover"
	
	return render(request,'home.html',{"images":images,"title":title})

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


@login_required
def create(request):
	
	current_user = request.user
	profile = Profile.objects.get(user = request.user.id)
	title = "Create New Post"
	if request.method == 'POST':
		form = NewImagePost(request.POST,request.FILES)
		if form.is_valid():
			post = form.save(commit =  False)
			post.profile = current_user
			post.user_profile = profile
			post.save()
			return redirect('profile',current_user.id)
	else:
		
		form = NewImagePost()

	return render(request,'my_accounts/create_post.html',{"form":form,"title":title})


@login_required
def comment(request, image_id):
	image = Image.get_image_by_id(image_id)
	if request.method == 'POST':
		form = CreateComment(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.image = image
			comment.profile = request.user
			comment.save()

			return redirect('home')
	else:
		form = CreateComment()

	return render(request, 'comments.html', {'form': form})