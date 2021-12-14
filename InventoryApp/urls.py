from django.urls import path
from .views import indexPageView, inventoryPageView, editPageView, createPageView, productDetailsPageView

urlpatterns = [
    path("", indexPageView, name = "index"), 
    path("inventory/", inventoryPageView, name = "inventory"),
    path("edit/", editPageView, name = "edit"),
    path("create/", createPageView, name = "create"),
    path("productdetails/", productDetailsPageView, name = "productdetails")
]