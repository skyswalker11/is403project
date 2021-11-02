from django.urls import path
from .views import indexPageView, inventoryPageView, editPageView, createPageView

urlpatterns = [
    path("", indexPageView, name = "index"), 
    path("inventory/", inventoryPageView, name = "inventory"),
    path("edit/<int:item_id>/", editPageView, name = "edit"),
    path("create/", createPageView, name = "create"),

]