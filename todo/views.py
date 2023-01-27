from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import *
from django.contrib import messages


def myview(request):
    context = {}
    obj = Todo.objects.all()

    if "all" in request.GET:
        all = request.GET.get('all')
        obj = Todo.objects.all()

    if "on" in request.GET:
        obj = obj.filter(
            status=True
        )

    if "off" in request.GET:
        obj = obj.filter(
            status=False
        )

    bt = request.GET.get('bt', None)
    at = request.GET.get('at', None)
    if bt:
        obj = obj.filter(
            deadline__gte=bt
        )

    if at:
        obj = obj.filter(
            deadline__lte=at
        )

    print(request.GET)
    context['todos'] = obj
    return render(request, 'index.html', context)


def add_view(request):
    context = {}
    form = ToDoForm()
    if request.method == "POST":
        form = ToDoForm(request.POST or None)
        if form.is_valid():
            new_task = form.save()
            messages.success(request, f"{new_task.task_name} added!")
            return redirect("todo:add")

    context['form'] = form
    return render(request, 'add.html', context)



