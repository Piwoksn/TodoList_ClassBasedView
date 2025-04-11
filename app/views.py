from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
class HomeView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "app/home_view.html"

class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "app/task_detail.html"


class CreateTask(CreateView):
    model = Task
    fields = "__all__"
    template_name = "app/newtask.html"
    success_url = reverse_lazy("home")

class EditTask(UpdateView):
    model = Task
    fields = "__all__"
    template_name = "app/newtask.html"
    success_url = reverse_lazy("home")

class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy("home")


class NewUser()