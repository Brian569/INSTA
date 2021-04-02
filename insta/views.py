from django.shortcuts import render, redirect
from .models import Profile, Image
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.method == 'GET':
        photos = Image.objects.all()

    context = {"photos": photos}

    return render(request, 'home.html', context)

@login_required
def my_profile(request):
    
    profile = request.GET.get('profile')
    if profile == None:
        photo = Image.objects.all()

    else:
        photo = Image.objects.filter(profile__name__contains=profile)

    profile = Profile.objects.all()

    context = {'profiles': profile, 'photos': photo}
    prof_temps = {''}

    return render(request, 'my_accounts/profile.html',context)

@login_required
def comments(request):
    if request.method == 'POST':
        commentss = request.POST['comment']
        comment = Image.objects.all()
        comment.create(comments=commentss)
        
        print('comment saved')    

    else:
        photo = Image.objects.all()
    

    context = { "photos" : photo}

    return render(request, 'comments.html', context)

def login(request):

    return render(request, 'my_accounts/login.html')

def register(request):

    
    return (request, 'my_accounts/register.html')


def likes(request, pk):
    if request.method == 'POST':
        like = request.POST['likes']
        liky = Image.objects.filter(pk = pk)
        liky.save()

        print(';like saved')

    else:
       liky = Image.objects.all() 

    return render(request, 'my_accounts/profile.html', {'likes': liky})


def logout_view(request):
    logout(request)
    return redirect('login')