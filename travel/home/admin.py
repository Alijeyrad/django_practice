from django.contrib import admin
from .models import Post, Contact, Category
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['title','id', 'author', 'counted_views', 'status', 'created_date']
    list_filter = ('status', 'author')
    search_fields = ['title','content']
    #ordering = ('-created_date',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass