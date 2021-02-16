from django.contrib import admin

# Register your models here.
from blog.models import BlogPost, Category

admin.site.register(BlogPost)
admin.site.register(Category)
