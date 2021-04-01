from camp import views
from django.urls import path

urlpatterns = [
    path('getList', views.campSite_list),
    path('getDetail/<int:pk>/', views.campSite_detail),
    path('camptaglist/<int:tag_id>', views.camptaglist),
    path('camplikeslist/', views.campLikesList),
    path('getwordresult/', views.campWordResult),
    path('gettagresult/', views.campTagResult),
    path('createreview/', views.campCreateReview),
    path('readreview/', views.campReadReview),
    path('deletereview/', views.campDeleteReview)
]