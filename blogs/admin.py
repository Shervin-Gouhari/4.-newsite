from django.contrib import admin
from .models import Post

# admin.site.register(Post)

# list_display can either be a list, or a tuple
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'status', 'publish')
    list_filter = ('status',)
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    list_editable = ('status',)
    