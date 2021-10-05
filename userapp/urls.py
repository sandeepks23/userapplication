from django.urls import path
from userapp.views import UserRegisterView,UserLoginView,HomePageView,UserLogoutView,ProfileView,UpdateProfile

urlpatterns = [
    path("register",UserRegisterView.as_view(),name="register"),
    path("login",UserLoginView.as_view(),name="signin"),
    path("home",HomePageView.as_view(),name="home"),
    path("logout",UserLogoutView.as_view(),name="signout"),
    path("profile",ProfileView.as_view(),name="profile"),
    path("updateprofile",UpdateProfile.as_view(),name="update")

]