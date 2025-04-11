from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("<int:pk>/", views.TaskDetail.as_view(), name="detail"),
    path("edit/<int:pk>/", views.EditTask.as_view(), name="edit"),
    path("delete/<int:pk>/", views.DeleteTask.as_view(), name="delete"),
    path("newtask/", views.CreateTask.as_view(), name="newtask"),
]
