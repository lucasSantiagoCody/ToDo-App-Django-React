from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.TodoRegisterView.as_view(), name='todo-register-view'),
    path('list/', views.TodoListView.as_view(), name='todo-list-view'),
]