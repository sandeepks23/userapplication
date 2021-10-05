from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.core.paginator import Paginator

from django.views.generic import TemplateView,CreateView,UpdateView,DetailView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout

from userapp.forms import UserRegisterForm,UserLogin
from postapp.models import Posts
from postapp.forms import AddPost
class UserRegistrationView(CreateView):
    model = User
    template_name = "registration.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")

class UserLoginView(TemplateView):
    template_name = "signin.html"
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
                return redirect("homepage")
            else:
                return render(request,self.template_name)
        return render(request,self.template_name)


class HomePageView(TemplateView):
    template_name = "home.html"

    context={}
    def get(self, request, *args, **kwargs):
        # posts = Posts.objects.order_by('-date')
        posts=Posts.objects.all().order_by('-id')
        paginator=Paginator(posts,4)
        page=request.GET.get('page')
        posts=paginator.get_page(page)

        self.context['posts']=posts


        return render(request,self.template_name,self.context)

class UserLogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")

class CreatePostView(TemplateView):
    template_name = 'createpost.html'
    context={}
    def get(self, request, *args, **kwargs):
        form=AddPost()
        self.context['form']=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        # my_post=request.POST['mypost']
        # post=Posts(post_owner=request.user,text_content=my_post)
        # post.save()
        # return redirect('homepage')
        if request.is_ajax:
            form=AddPost(request.POST)
            if form.is_valid():
                # text_content=form.cleaned_data.get('text_content')
                # post=Posts(post_owner=request.user,text_content=text_content)
                # instance=post.save()
                instance=form.save(commit=False)
                instance.post_owner=request.user
                instance.save()
                ser_instance = serializers.serialize('json', [instance])
                # send to client side.
                return JsonResponse({"instance": ser_instance}, status=200)

            else:
                # some form errors occured.
                return JsonResponse({"error": form.errors}, status=400)
        return JsonResponse({'error': ''}, status=400)



class ViewPost(TemplateView):
    # template_name = 'postdetail.html'
    # model = Posts
    # context_object_name = "post"
    template_name = "postdetail.html"
    context={}
    def get(self, request, *args, **kwargs):
        id=kwargs["pk"]
        post=Posts.objects.get(id=id)
        self.context["post"]=post
        liked=False
        if post.likes.filter(id=self.request.user.id).exists():
            liked=True
        self.context['liked']=liked
        return render(request,self.template_name,self.context)

class LikeView(TemplateView):
    template_name = 'postdetail'
    def post(self, request, *args, **kwargs):
        id=kwargs['pk']
        post=Posts.objects.get(id=id)
        is_liked=False
        for like in post.likes.all():
            if like==request.user:
                is_liked=True
                break
        if is_liked:
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        like_count=len(post.likes.all())
        post.like_count=like_count
        post.save()

        return redirect('viewpost',post.id)

