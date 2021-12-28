from django.contrib import admin
from .models import TodoList, Item
# Register your models here.
admin.site.register(TodoList)  #Gives acces from admin page to TodoList database
#admin.site.register(Item)


class ItemAdmin(admin.ModelAdmin):
	fieldsets = [
		('Item', {'fields': ['text','todolist']}),
		('Date information', {'fields': ['creation_date']}),
		('State',{'fields': ['priority','complete']})]
	list_display = ('text', 'creation_date', 'priority', 'complete') # adds extra features to show on lins mode
	list_filter = ['creation_date'] # adds a filter table
	search_fields = ['text'] # adds a search box

	#fields = ['todolist', 'text','creation_date', 'priority','complete'] #no order

admin.site.register(Item, ItemAdmin)

