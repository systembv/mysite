from django.urls import path

from . import views

urlpatterns = [
    path('', views.tasklist, name="task-lista"),
    path("task/<int:id>", views.taskView, name="task-view"),
    path("addtask/", views.newTask, name="new-task"),
    path("edit/<int:id>", views.editTask, name="edit-task"),
    path('changestatus/<int:id>', views.changeStatus, name="change-status"),
    path("delete/<int:id>", views.deleteTask, name="delete-task"),
]
