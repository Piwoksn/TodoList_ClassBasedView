from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("<int:pk>/", views.TaskDetail.as_view(), name="detail"),
    path("edit/<int:pk>/", views.EditTask.as_view(), name="edit"),
    path("delete/<int:pk>/", views.DeleteTask.as_view(), name="delete"),
    path("newtask/", views.CreateTask.as_view(), name="newtask"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("signup/", views.SignupUser.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(next_page= "login"), name="logout"),
]