from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    path('account_settings',views.account_settings,name='account_settings'),
    path('upload',views.upload,name='upload'),
    path('like-post',views.like_post,name='like-post'),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('follow',views.follow,name='follow'),
]