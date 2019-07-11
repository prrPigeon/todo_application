from django.urls import path
from . import views 

urlpatterns = [
	path('', views.home, name='home'),
	path('added', views.addTodo, name='added'),
	path('completed/<todo_id>', views.completeTodo, name='completed'),
	path('deletecompleted', views.deleteCompleted, name='deletecompleted'),
	path('deleteall', views.deleteAll, name='deleteall')
]