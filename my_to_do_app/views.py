from django.shortcuts import render,redirect
from .models import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    todos = Todo.objects.all()
    content = {'todos':todos}
    return render(request,'my_to_do_app/index.html',content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))

def deleteTodo(request):
    done_todo_id = request.GET['todoNum']
    #print("완료한 todo의 id",done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.delete()
    return redirect('index')