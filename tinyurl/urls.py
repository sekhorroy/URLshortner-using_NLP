
from django.urls import path, include, re_path
from . import views
app_name = "tinyurl"

urlpatterns = [
    path('', views.index, name='index'),
    path('redirect/', views.re_direct_url, name='redirect'),
    path('makeshort/', views.shorten_url, name='shorten_url'),
]






