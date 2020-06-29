from django.urls import path

from . import views

urlpatterns = [
    path("pizza", views.pizza, name="pizza"),
    path("pasta", views.pasta, name="pasta"),
    path("subs", views.subs, name="subs"),
    path("salads", views.salads, name="salads"),
    path('dinnerplatters', views.dinner_platters, name="dinner_platters"),
    path("added", views.added, name="added"),
    path("cart", views.cart, name="cart"),
    path("delete", views.delete, name="delete"),
    path("placeorder", views.place_order, name="place_order"),
    path("confirmorder", views.confirm_order, name="confirm_order")
]
