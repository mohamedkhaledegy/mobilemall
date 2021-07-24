from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('',views.index , name='index' ),
    path('brands/',views.all_brands , name='all_brands' ),
    path('mobiles/<slug:slug>/',views.brand_mobs , name='brand_mobiles' ),
    path('spares/<slug:slug>/' , views.brand_sprs , name='brand_spares'),
    path('<slug:slug>/',views.single_device , name='single_device' ),

    ]