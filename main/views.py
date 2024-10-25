from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request,'index.html')


def timer_page(request):
    return render(request, 'timer-page.html')


def sign_in(request):
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(request, username=login, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid login or password.")
    
    return render(request, "sign-in.html")  # Adjust if your template has a different name

