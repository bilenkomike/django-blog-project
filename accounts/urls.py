from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]