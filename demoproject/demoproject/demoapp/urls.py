from . import views
from django.urls import path, include

urlpatterns = [

    path('hello',views.hello,name='hello'),
    path('demo1/', views.demo1, name='demo1'),
    path('demo2', views.demo2, name='demo2'),
    path('demo3', views.demo3, name='demo3'),
    path('demo4', views.demo4, name='demo4'),
]
