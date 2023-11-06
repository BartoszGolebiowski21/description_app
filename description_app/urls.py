from django.urls import path

from . import views

urlpatterns = [
    path("", views.AddChildView.as_view(), name="add-child"),
    path("all-children", views.AllChildrenView.as_view(), name="all-children"),
    path("child-detail/<int:pk>", views.SingleChildView.as_view(), 
         name="child-detail"),
    path("child-detail/<int:pk>/edit-child", views.EditChildView.as_view(), 
         name="edit-child"),
    path("child-detail/<int:pk>/delete-child", views.DeleteChildView.as_view(), 
        name="delete-child"),
]