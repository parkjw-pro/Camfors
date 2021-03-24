from camp import views
from django.urls import path

urlpatterns = [
    path('getList', views.campSite_list),
    path('getDetail/<int:pk>/', views.campSite_detail),
    path('camptaglist/<int:tag_id>', views.camptaglist),
]