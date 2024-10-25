from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser  # Import your CustomUser model
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request,'index.html')


def timer_page(request):
    return render(request, 'timer-page.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser  # Ensure this import is correct

def sign_in(request):
    if request.method == "POST":
        login_input = request.POST.get("login")  # Username or phone number
        password = request.POST.get("password")

        # Debugging output
        print(f"Login input: {login_input}, Password: {password}")

        # Try to authenticate using username first
        user = authenticate(request, username=login_input, password=password)
        print(user)

        if user is None:
            # Check if the login input is a phone number
            try:
                user = CustomUser.objects.get(phone_number=login_input)
                # Check password manually if found by phone number
                if user.check_password(password):
                    login(request, user)  # Correctly log in the user
                    return redirect("home")  # Redirect to home page
                else:
                    messages.error(request, "Invalid password.")  # Password mismatch
            except CustomUser.DoesNotExist:
                messages.error(request, "Invalid username or password.")  # User not found

        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "sign-in.html")  # Render the sign-in page for GET requests



