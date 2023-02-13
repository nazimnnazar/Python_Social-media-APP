from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='signin')
def home(request):
    user_profile = Profile.objects.get(user=request.user)
    context = {
        'user_profile':user_profile
    }
    return render(request,'index.html',context)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email alredy exiest..Try another one')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username alredy exiest..Try another one')
                return redirect('signup') 
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                user_login = auth.authenticate(username=username,password=password)
                auth.login(request, user_login)
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('account_settings')
        else:
            messages.info(request, 'Password Not Maching')
            return redirect('signup')         
    else:
        return render(request, 'core/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'User OR Password in correct')
            return redirect('signin')
    else:
        return render(request,'core/login.html')

def logout(request):
    auth.logout(request)
    return redirect('signin')

def account_settings(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        if request.FILES.get('image')==None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('image') !=None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        return redirect('account_settings')
    return render(request, 'core/settings.html',{'user_profile':user_profile})

def upload_post(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['captiom']
        new_post = Post.objects.create(user=user,image=image,caption=caption)
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')