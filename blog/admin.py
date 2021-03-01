from django.contrib import admin

# importing all models to register
from .models import Category, Blog, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'created_at']
    list_editable = ('status',)
    list_per_page = 10
    
    
admin.site.register(Category, CategoryAdmin)



class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'category', 'tag', 'created_at']
    list_per_page = 20
    list_filter = ('category',)
    list_editable = ('status', 'category', 'tag',)
    search_fields = ('title', 'category',)

admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'message']
    list_per_page = 20

admin.site.register(Comment, CommentAdmin)