from django.urls import path
from django.views.generic import TemplateView, RedirectView
from django.contrib import admin
from src.products.views import DigitalProductListView, ProductListView, ProtectedProductDetailView, ProtectedProductListView

urlpatterns = [ # type: ignore
    path("admin/", admin.site.urls), 
    path("about/", TemplateView.as_view(template_name="about.html")),
    path("about-us/", RedirectView.as_view(url="/about/")),
    path("products/", ProductListView.as_view()), 
    path("digital-products/", DigitalProductListView.as_view()), 
    path("my-products/<slug:slug>/", ProtectedProductDetailView.as_view()), 
    path("my-products/", ProtectedProductListView.as_view()), #<---- Added this line
]
