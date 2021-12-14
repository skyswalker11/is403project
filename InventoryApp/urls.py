from django.urls import path
from .views import indexPageView, inventoryPageView, editPageView, createPageView

urlpatterns = [
    path("", indexPageView, name = "index"), 
    path("inventory/", inventoryPageView, name = "inventory"),
    path("edit/", editPageView, name = "edit"),
    path("create/", createPageView, name = "create"),

]

    #    urlpatterns = [ 
    #         path("<str:sName>/<int:iAge>", agePageView, name="register_age"), 
    #         path("<str:sName>/", namePageView, name="register_name"),
    #         path("", defaultPageView, name="register"),
    #     ]