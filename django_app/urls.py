from django.urls import path
from django_app import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),


    #TODO главная система
    path('listsuggest/', views.list_suggests, name='listsuggest'),
    path('sendsuggest/', views.suggest_create, name='suggest_create'),
    path('detail/<str:pk>/', views.post_detail, name="post_detail"),
    path('delete/<str:pk>/', views.post_delete, name="post_delete"),
    path("post/comment/create/<str:pk>/", views.post_comment_create, name="post_comment_create"),

    path('post/comment/vote/<str:pk>/<str:vote>/', views.vote_comment, name='vote_comment'),


    #todo Аутинтефикация
    path('login/', views.login_f, name='login'),
    path('logout/', views.logout_f, name='logout'),
    path('register/', views.register_f, name='register'),
]