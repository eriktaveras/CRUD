from multiprocessing import context
from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class HomeView(ListView):
    model = Task
    template_name = "home.html"
    ordering = ['-id']
    paginate_by = 5

class TaskCreateView(CreateView):
    model = Task
    fields = ['content']
    template_name = "create.html"
    success_url = "/"

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['content']
    template_name = 'update.html'
    success_url = '/'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = '/'

