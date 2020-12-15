from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='blog-home'),
    path('about/', views.about,name='blog-about'),
    path('create/',views.blog_create,name='blog-create'),
    path('<slug:slug>/',views.blog_detail,name='blog-detail'),
]
