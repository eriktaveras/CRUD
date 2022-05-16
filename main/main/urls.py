
from django.contrib import admin
from django.urls import path
from todo.views import TaskCreateView, TaskUpdateView, TaskDeleteView
from todo.views import HomeView, TaskDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('create/', TaskCreateView.as_view()),
    path('task/<pk>/', TaskDetailView.as_view() ),
    path('task/<pk>/update', TaskUpdateView.as_view()),
    path('task/<pk>/delete', TaskDeleteView.as_view())

]
