from . import views
from django.urls import path

urlpatterns = [
    path('getList', views.campsitelist),
    path('getDetail/<int:pk>/', views.campsitedetail),
    path('camptaglist/<int:tag_id>', views.camptaglist),
    path('camplikeslist/', views.camplikeslist),
    path('getwordresult/', views.campwordresult),
    path('gettagresult/', views.camptagresult),

    path('gettaglist', views.gettaglist),
    path('listbyuser/<int:user_id>/', views.listbyuser),
    path('camppoptag', views.camppoptagresult),

    path('addlike', views.addlike),
    path('unlike', views.unlike),
    path('getlikeinfo/', views.getlikeinfo),

    path('camprecommend/<int:campsite_id>/', views.camprecommend),
    path('createreview', views.campcreatereview),
    path('readreview/<int:campsite_id>/', views.campreadreview),
    path('deletereview/<int:review_id>/', views.campdeletereview)

]