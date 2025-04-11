from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

# Create your views here.
class LoginUser(LoginView):
    template_name = "app/login.html"
    fields = "__all__"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("home")

class CreateUser(FormView):
    template_name = "app/signup.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    


class HomeView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "app/home_view.html"
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(completed = False).count() 
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"
    template_name = "app/task_detail.html"


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "content", "completed"]
    template_name = "app/newtask.html"
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)
    

class EditTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "content", "completed"]
    template_name = "app/newtask.html"
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("home")


