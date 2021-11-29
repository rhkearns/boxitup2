from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('boxes/', views.boxes_index, name='boxes_index'),
  path('boxes/<int:box_id>/', views.boxes_detail, name='boxes_detail'),
  path('boxes/create/', views.BoxCreate.as_view(), name='boxes_create'),
  path('boxes/<int:pk>/update', views.BoxUpdate.as_view(), name='boxes_update'),
  path('boxes/<int:pk>/delete', views.BoxDelete.as_view(), name='boxes_delete'),
  path('boxes/<int:box_id>/add_item', views.add_item, name='add_item'),
  path('boxes/<int:box_id>/delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
  path('boxes/<int:box_id>/close', views.close_box, name="close_box"),
  path('items/index/', views.items_index, name="items_index"),
  path('accounts/signup/', views.signup, name='signup'),
]