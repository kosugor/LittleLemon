# define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("items/", views.MenuItemsView.as_view()),
    path("item/<int:pk>", views.SingleMenuItemView.as_view()),
]
