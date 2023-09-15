
from django.urls import path

from .  import views

app_name='shopp'


urlpatterns = [

    path('',views.allproduct,name='allproduct'),
    path('<slug:c_slug>/',views.allproduct,name='productbycategory'),
    path('<slug:c_slug>/<slug:product_slug>/', views.productDetail, name='productdetails'),

]
