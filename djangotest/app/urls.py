from django.urls import path
from django.views.generic import ListView, DetailView
from . import views
from .models import News
from .views import NewsListView, CategoryNewsListView, CategoryListView

urlpatterns = [
    path('', NewsListView.as_view(), name='index'),
    path('<int:pk>', DetailView.as_view(model=News, template_name="app/news_view.html")),
    path('category/<category_name>', CategoryNewsListView.as_view()),
    path('categories', CategoryListView.as_view(), name='categories'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('news_add', views.create, name='news_add'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('gallery', views.gallery, name='gallery'),
    path('feedback', views.feedback, name='feedback'),
    path('profile', views.profile, name='profile'),
    path('search', views.search, name='search'),
]
