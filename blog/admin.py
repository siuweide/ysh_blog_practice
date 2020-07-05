from django.contrib import admin
from blog.models import Blog, BlogType

@admin.register(BlogType)
class BlogType(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    ordering = ('id', )

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blog_type', 'content', 'get_read_num', 'created_time', 'updated_time')
    ordering = ('id', )

# @admin.register(ReadNum)
# class ReadNumAdmin(admin.ModelAdmin):
#     list_display = ('read_num', 'blog')
