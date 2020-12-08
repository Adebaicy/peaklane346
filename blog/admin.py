from django.contrib import admin

# Register your models here.
from blog.models import News




@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}



