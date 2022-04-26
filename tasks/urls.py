from django.urls import path
from .views import TasksList, TaskDetails, CreateTasks, UpdateTask, DeleteTask, WelcomePage, deleteCompleted

urlpatterns = [
    path('', WelcomePage.as_view(), name='welcome'),
    path('tasks-list/', TasksList.as_view(), name="tasks-list"),
    path('tasks-detail/<int:pk>/', TaskDetails.as_view(), name="task-details"),
    path('add-tasks/', CreateTasks.as_view(), name="add-tasks"),
    path('update-tasks/<int:pk>/', UpdateTask.as_view(), name="update-tasks"),
    path('delete-tasks/<int:pk>/', DeleteTask.as_view(), name="delete-task"),
    path('delete-completed/', deleteCompleted, name="delete-completed"),
]