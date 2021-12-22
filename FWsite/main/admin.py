from django.contrib import admin
from .models import TodoList
# Register your models here.
admin.site.register(TodoList)  #Gives acces from admin page to TodoList database