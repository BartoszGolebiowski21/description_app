from django.urls import path

from . import views

urlpatterns = [
    path("", views.generate_description, name="generate_description"),
    path("all-children", views.AllChildrenView.as_view(), name="all-children"),
    path("child-detail/<int:pk>", views.SingleChildView.as_view(), 
         name="child-detail"),
]