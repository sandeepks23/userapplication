from django.urls import path
from postapp.views import UserRegistrationView,UserLoginView,HomePageView,CreatePostView,LikeView,UserLogoutView,ViewPost

urlpatterns=[
    path('registration',UserRegistrationView.as_view(),name='reg'),
    path('',UserLoginView.as_view(),name='login'),

    path('homepage',HomePageView.as_view(),name='homepage'),
    path('createpost',CreatePostView.as_view(),name='createpost'),
    path('post/<int:pk>',ViewPost.as_view(),name='viewpost'),
    path('like/<int:pk>',LikeView.as_view(),name='like'),
    path('signout',UserLogoutView.as_view(),name='logout'),
    # path('newpost',AddPostView.as_view(),name='newpost')

]