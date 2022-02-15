from django.contrib import admin
from .models import Post, Contact
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['id','title', 'counted_views', 'status', 'created_date']
    list_filter = ('status',)
    search_fields = ['title','content']
    #ordering = ('-created_date',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass