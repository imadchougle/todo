from django.contrib import admin
from django.urls import path
from todo import views

# urls.py
from django.urls import path, include
from todo import views

urlpatterns = [
    path('', views.index, name="todo"),
    path('admin/', admin.site.urls),
    path('update_status/<int:todo_id>/', views.update_status, name='update_status'),
    path('api/', include('todo.urls')),
]


