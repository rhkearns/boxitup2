from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('boxes/', views.boxes_index, name='boxes_index'),
  path('boxes/<int:box_id>/', views.boxes_detail, name='boxes_detail'),
  path('boxes/create/', views.BoxCreate.as_view(), name='boxes_create'),
  path('boxes/<int:pk>/update', views.BoxUpdate.as_view(), name='boxes_update'),
  path('boxes/<int:pk>/delete', views.BoxDelete.as_view(), name='boxes_delete'),

]