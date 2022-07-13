from multiprocessing import context
from operator import index
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from tkinter import *
def task(request):
    tasks = details.objects.all()
    forms = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks':tasks,'form':forms}
    return render(request,'work/index.html',context)
def update(request,pk):
    task = details.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')    
    context={'form':form}
    return render(request,'work/update.html',context)
def delete(request,pk):
    task = details.objects.all()
    item = details.objects.get(id=pk)  
    if request.method == 'POST':
        item.delete()
        return redirect('/') 
    context = {'item':item,'task':task}
     
    return render(request,'work/delete.html',context)

