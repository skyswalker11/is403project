from django.urls import path
from .views import indexPageView, inventoryPageView, editPageView, putPageView, deletePageView, createPageView, productDetailsPageView

urlpatterns = [
    path("", indexPageView, name = "index"), 
    path("inventory/", inventoryPageView, name = "inventory"),
    path("edit/<int:product_id>", editPageView, name = "edit"),
    path("put/", putPageView, name = "put"),
    path("delete/", deletePageView, name = "delete"),
    path("create/", createPageView, name = "create"),
    path("productdetails/<int:product_id>", productDetailsPageView, name = "productdetails")
]