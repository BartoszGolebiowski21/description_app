from django.urls import path

from . import views

urlpatterns = [
    path("", views.AddChildView.as_view(), name="add-child"),
    path("all-children", views.AllChildrenView.as_view(), name="all-children"),
    path("child-detail/<int:pk>", views.SingleChildView.as_view(), 
         name="child-detail"),
]