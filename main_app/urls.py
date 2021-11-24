from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('boxes/', views.boxes_index, name='boxes_index'),
]