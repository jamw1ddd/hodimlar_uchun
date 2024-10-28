from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser  # Import your CustomUser model
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request,'index.html')

def boshqich1_view(request):
    return render(request,'bosqich1.html')


def timer_page(request):
    return render(request, 'timer-page.html')


def sign_in(request):
    if request.method == "POST":
        login_input = request.POST.get("login")  
        password = request.POST.get("password")

        user = authenticate(request, username=login_input, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "sign-in.html")  



from django.shortcuts import render, redirect
from django.utils import timezone
import datetime

# Timer duration in seconds (1 minute for testing)
TIMER_DURATION = 60  # 60 seconds = 1 minute

def home(request):
    # Check if the timer has started
    if request.session.get('start_time'):
        # Convert timestamp back to datetime and make it timezone-aware
        start_time = timezone.make_aware(datetime.datetime.fromtimestamp(request.session['start_time']))
        elapsed_time = (timezone.now() - start_time).total_seconds()
        timer_expired = elapsed_time >= TIMER_DURATION
    else:
        timer_expired = False

    return render(request, 'home.html', {'timer_expired': timer_expired})

def timer(request):
    # Handle POST request to start the timer
    if request.method == 'POST':
        # Set the start time only if it has not been set yet
        if not request.session.get('start_time'):
            request.session['start_time'] = timezone.now().timestamp()  # Store timestamp instead of datetime

    # Calculate remaining time if the timer is running
    start_time = request.session.get('start_time')
    if start_time:
        elapsed_time = (timezone.now().timestamp() - start_time)  # Use timestamp for calculations
        remaining_time = max(0, TIMER_DURATION - elapsed_time)

        # Redirect to home if the timer has expired
        if elapsed_time >= TIMER_DURATION:
            request.session.pop('start_time', None)  # Reset start time
            return redirect('home')

        return render(request, 'timer.html', {'remaining_time': remaining_time})

    # If no start time, redirect to home
    return redirect('home')
