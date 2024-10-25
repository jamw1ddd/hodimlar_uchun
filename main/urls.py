from django.urls import path
from main.views import home_view,timer_page,sign_in


urlpatterns = [
    path('',home_view,name='home'),
    path("sign-in/",sign_in, name="sign_in"),
    path('timer/',timer_page,name='timer'),
]

