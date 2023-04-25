from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Profile, Dweet
from .forms import DweetForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


# Create your views here.

# Auth

def home(request):
    return render(request, 'auth/loginuser.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'auth/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                user.save()
                login(request, user)
                return redirect("dwitter:dashboard")
            
            except IntegrityError:
                return render(request, 'auth/signupuser.html', {'form':UserCreationForm(), 'error': 'That username has already been taken'})
        else:
            return render(request, 'auth/signupuser', {'form':UserCreationForm, 'error': 'Password did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'auth/loginuser.html', {'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'auth/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect("dwitter:dashboard")
        
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('dwitter:home')
    

# Dwitter 

@login_required
def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:dashboard")
        
    followed_dweets = Dweet.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by("-created_at")

    return render(
        request,
        "dwitter/dashboard.html",
        {"form": form, "dweets": followed_dweets},
    )

@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles":profiles})

@login_required
def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile":profile})