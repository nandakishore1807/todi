from django import views
from django.urls import URLPattern, path
from .views import *
from tkinter import *

urlpatterns = [
    path('',task),
    path('update/<str:pk>/',update,name='task_update'),
    path('delete/<str:pk>/',delete,name='task_delete')

]
