from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView

from .models import Task


class WelcomePage(TemplateView):
    template_name = 'welcome.html'


class TasksList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetails(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'


class CreateTasks(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'tasks/task_create.html'
    success_message = "Task was added successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateTask(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'tasks/update_tasks.html'
    success_message = "Task was updated/completed successfully"


class DeleteTask(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('tasks-list')
    success_message = "Task was deleted successfully"


def Completed(request, pk):
    task = Task.objects.get(id=pk)
    if not task.completed:
        task.completed = True
        task.save()
        return redirect('tasks-list')
    context = {task: "task"}
    return render(request, 'tasks/task_detail.html', context)


def deleteCompleted(request):
    delete = Task.objects.filter(completed__exact="True")
    if delete:
        delete.delete()
        return redirect('tasks-list')
    context = {"delete": delete}
    return render(request, context)
