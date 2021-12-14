from django.urls import path
from .views import indexPageView, inventoryPageView, editPageView, createPageView, productDetailsPageView, putPageView

urlpatterns = [
    path("", indexPageView, name = "index"), 
    path("inventory/", inventoryPageView, name = "inventory"),
    path("edit/<int:product_id>", editPageView, name = "edit"),
    path("put/", putPageView, name = "put"),
    path("create/", createPageView, name = "create"),
    path("productdetails/<int:product_id>", productDetailsPageView, name = "productdetails")
]