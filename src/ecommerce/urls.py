from django.urls import path

from ecommerce import views

urlpatterns = [
    path("", views.product_model_list_view, name="product_model_list_view"),
    path("<int:product_id>/", views.product_model_detail_view, name="product_model_detail_view"), 
    path("create/", views.product_model_create_view, name="product_model_create_view"), 
    path("<int:product_id>/update/", views.product_model_update_view, name="product_model_update_view"),
    path("<int:product_id>/delete/", views.product_model_delete_view, name="product_model_delete_view"), #<-- Added delete view URL
]

