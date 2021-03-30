from user import views
from django.urls import path

urlpatterns = [
    path('signup', views.signup),
    path('delete', views.delete),
    path('login', views.login),
    path('logout', views.logout),
    path('session', views.session),
]