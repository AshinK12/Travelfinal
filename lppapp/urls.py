from . import views
from django.urls import path
from lppproject import settings

urlpatterns = [
    path('', views.demo, name='demo'),
    path('index.html', views.hom, name='hom'),
    path('about/', views.about, name='about'),
]



