from django.urls import path

from . import views

urlpatterns = [

    path('',views.hello,name='hello'),
    path('delt<int:id>/', views.delete, name='delt'),
    path('update<int:id>/', views.update, name='update'),
    path('view/', views.viewlist.as_view(), name='view'),
    path('diew<int:pk>/', views.detailview.as_view(), name='dview'),
    path('updview<int:pk>/', views.updateview.as_view(), name='updview'),
    path('delete<int:pk>/', views.detailview.as_view(), name='delete'),

]