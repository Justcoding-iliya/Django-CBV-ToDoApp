from django.shortcuts import render
from .models import Task
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from ToDo.forms import TaskUpdateForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/task_list.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    
    
class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ["title"]
    success_url = reverse_lazy("ToDo:task-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task 
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('ToDo:task-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    success_url = reverse_lazy("ToDo:task-list")
    template_name = 'todo/task_update_form.html'
    form_class = TaskUpdateForm


class TaskComplate(LoginRequiredMixin,View):
    model = Task
    success_url = reverse_lazy("ToDo:task-list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complate = True
        object.save()
        return redirect(self.success_url)




                                                   
