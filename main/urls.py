from django.urls import path
from main.views import home_view,timer_page,sign_in,boshqich1_view,home,timer


urlpatterns = [
    path('',home_view,name='homee'),
    path("sign-in/",sign_in, name="sign_in"),
    path('bosqich1/',boshqich1_view,name='boshqich1'),
    path('home/', home, name='home'),
    path('timer/', timer, name='timer'),
]

