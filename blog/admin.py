from django.contrib import admin
from .models import *


# admin.site.register(Post)
# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    prepopulated_fields = {"slug":("name",)}
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(UserData)


