from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from .models import UserProfile
from django.views.generic import DetailView

def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            address = form.cleaned_data.get('address')
            profile = form.cleaned_data.get('profile')

            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            user_profile = UserProfile.objects.create(user=user, address=address, profile=profile)

            messages.success(request, 'Your account has been successfully created.')
            return redirect('signin')
        else:
            print(form.errors)

    else:
        form = SignUpForm()

    return render(request, 'authentication/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            # user = get_object_or_404(User)
            context = {'user': user}
            print(dir(user))
            return render(request, "authentication/index.html", context)
        else:
            messages.error(request, "Bad credentials")
            return redirect('home')
    
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')
