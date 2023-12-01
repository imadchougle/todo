# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import TodoForm
from .models import Todo

def index(request):
    item_list = Todo.objects.order_by("-date")

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.status = 'OPEN'  # Set default status to OPEN
            todo.save()
            return redirect('todo')

    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }

    return render(request, 'todo/index.html', page)

def update_status(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    if request.method == "POST":
        status = request.POST.get('status')
        todo.status = status
        todo.save()
        messages.success(request, 'Status updated successfully.')
        return redirect('todo')

    return render(request, 'todo/update_status.html', {'todo': todo})
