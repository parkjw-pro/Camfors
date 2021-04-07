from . import views
from django.urls import path

urlpatterns = [
    path('signup', views.signup),
    path('delete', views.delete),
    path('login', views.login),
    path('logout', views.logout),
    path('email', views.checkEmail),
    path('like', views.like),
    path('review', views.review),
]