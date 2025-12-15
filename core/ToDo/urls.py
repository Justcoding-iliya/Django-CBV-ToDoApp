from django.urls import path
from . import views

app_name = "ToDo"

urlpatterns = [
    path("",views.TaskList.as_view(),name="task-list"),
    path("create/",views.TaskCreate.as_view(),name="task-create"),
    path("update/<int:pk>/",views.TaskUpdate.as_view(),name="task-update"),
    path("delete/<int:pk>/",views.TaskDelete.as_view(),name="task-delete"),
    path("complate/<int:pk>/",views.TaskComplate.as_view(),name="task-complate"),
]