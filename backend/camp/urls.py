from camp import views
from django.urls import path

urlpatterns = [
    path('getList', views.campSite_list),
    path('getDetail/<int:pk>/', views.campSite_detail),
    path('camptaglist/<int:tag_id>', views.camptaglist),
    path('camplikeslist/', views.campLikesList),
    path('getwordresult/', views.campWordResult),
    path('gettagresult/', views.campTagResult),
<<<<<<< HEAD
    path('addlike', views.addlike),
    path('unlike', views.unlike),
    path('getlikeinfo/', views.getlikeinfo)
=======
    path('addlike/',views.addlike),
    path('createreview', views.campCreateReview),
    path('readreview/<int:campsite_id>/', views.campReadReview),
    path('deletereview/<int:review_id>/', views.campDeleteReview)
>>>>>>> da34a12757ade6f75ab8fb289765badb0bc9fa91
]