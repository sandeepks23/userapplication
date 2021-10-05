from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,UpdateView,DetailView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout

from userapp.forms import UserRegisterForm,UserLogin,UserUpdateForm
# Create your views here.



class UserRegisterView(CreateView):
    model = User
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("signin")

class UserLoginView(TemplateView):
    template_name = "login.html"
    context={}
    def get(self, request, *args, **kwargs):
        form = UserLogin()
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=UserLogin(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                return render(request,self.template_name)
        return render(request,self.template_name)


class HomePageView(TemplateView):
    template_name = "homepage.html"
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

class UserLogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("signin")


class ProfileView(TemplateView):
    template_name = "viewprofile.html"
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

class UpdateProfile(TemplateView):
    template_name = "updateprofile.html"
    context={}
    def get(self, request, *args, **kwargs):
        instance={
            "username":request.user.username,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
        }
        form=UserUpdateForm(initial=instance)
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=UserUpdateForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            request.user.username=username
            request.user.first_name=first_name
            request.user.last_name = last_name
            request.user.email=email
            request.user.save()
            return redirect("profile")





