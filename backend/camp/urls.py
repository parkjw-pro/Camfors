from camp import views
from django.urls import path, include

urlpatterns = [
    path('camp/', views.campSite_list),
    path('camp/<int:pk>/', views.campSite_detail),
]