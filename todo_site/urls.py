from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name="todo"),
    path('admin/', admin.site.urls),
]
