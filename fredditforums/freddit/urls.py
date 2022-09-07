from django.urls import path
from freddit import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_thread/', views.add_thread, name = 'add_thread'),
    path('thread/<slug:thread_slug>/', views.view_thread, name="thread_post")
]