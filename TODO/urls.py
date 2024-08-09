from django.urls import path
from .import views

urlpatterns = [
     #addTask
     path('addTask/',views.addTask,name='addTask'),
     #Mark as done
     path('Mark_as_done/<int:pk>/',views.Mark_as_done,name='Mark_as_done'),
     #undo
     path('Undo/<int:pk>/',views.Undo,name='Undo'),
     #edit function
     path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
     #delete Task
     path('delete_task/<int:pk>/',views.delete_task,name='delete_task'),
]