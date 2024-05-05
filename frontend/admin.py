from django.contrib import admin
from .models import Category,Post


class CategoryInline(admin.StackedInline):
    model=Post 
    extra=1

class CategoryAdmin(admin.ModelAdmin):
    inlines=[CategoryInline]   
    list_display=['name','order']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post)
