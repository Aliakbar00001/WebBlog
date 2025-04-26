from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('signout/', views.signout, name='signout'),
    path('signup_success/', views.signup_success, name='signup_success'),
    re_path(r'^profile/(?P<username>[-_\w.]+)/$', views.profile, name='profile'),
    re_path(r'^profile/(?P<username>[-_\w.]+)/edit/$', views.profile_settings, name='profile_settings'),
    re_path(r'^profile/(?P<username>[-_\w.]+)/followers/$', views.followers, name='followers'),
    re_path(r'^profile/(?P<username>[-_\w.]+)/following/$', views.following, name='following'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post, name='post'),
    path('post/', views.post_picture, name='post_picture'),
    path('explore/', views.explore, name='explore'),
    path('notifications/', views.notifications, name='notifications'),
    path('inbox/', views.inbox, name='inbox'),
    re_path(r'^inbox/(?P<label>[-_\w.]+)/$', views.chat, name='chat'),
    path('new_chat/', views.new_chat, name='new_chat'),
    re_path(r'^new_chat/(?P<username>[-_\w.]+)/$', views.new_chat_create, name='new_chat_create'),
    re_path(r'^post/(?P<pk>\d+)/likes/$', views.likes, name='likes'),
    path('like/', views.add_like, name='like'),
    path('comment/', views.add_comment, name='comment'),
    path('follow_toggle/', views.follow_toggle, name='follow_toggle'),
]
