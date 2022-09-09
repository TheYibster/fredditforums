from unicodedata import name
from django.urls import path
from freddit import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_thread/', views.add_thread, name = 'add_thread'),
    path('thread/<slug:thread_slug>/', views.view_thread, name="thread_post"),
    path('thread/<thread_slug>/add_comment/', views.add_comment, name="add_comment"),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name="logout_user"), 
    path('register_user/', views.register_user, name="register_user"),
    path('search/', views.search, name='search'),
    
]