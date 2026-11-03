
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile, DailyTracker
from django.utils import timezone


def home(request):
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            profile = None

        return render(request, 'accounts/dashboard.html', {
            'profile': profile
        })

    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        messages.error(request, 'Username ya password galat hai.')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile saved successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'accounts/profile.html', {
        'form': form
    })

0

@login_required
def diet(request):
    return render(request, 'accounts/diet.html')
0

@login_required
def exercise(request):
    return render(request, 'accounts/exercise.html')
0

@login_required
def recipes(request):
    return render(request, 'accounts/recipes.html')

@login_required
def tracker(request):
    today = timezone.localdate()
    tracker_data, created = DailyTracker.objects.get_or_create(user=request.user, date=today)
    fields = ["breakfast", "lunch", "dinner", "water", "fruits", "activity", "relaxation", "sleep"]
    if request.method == "POST":
        for field in fields:
            setattr(tracker_data, field, request.POST.get(field) == "on")
        tracker_data.save()
        return redirect("tracker")
    return render(request, "accounts/tracker.html", {"tracker": tracker_data})
    return render(request, 'accounts/tracker.html')

