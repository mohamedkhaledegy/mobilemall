from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('',views.index1 , name='index1' ),
    path('<slug:slug>',views.single_product , name='product' ),
    path('brand/<str:brd>',views.brand_devices , name='brand-mobiles' ),
    path('spares',views.brand_spares , name='brand-spares' ),
    path('accessories',views.brand_accessories , name='brand-accessories' ),
    path('brands',views.brands_list , name='brands' ),
]