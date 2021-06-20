from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('',views.index1 , name='index1' ),
    path('samasung-note-20',views.single_product , name='product' ),
]