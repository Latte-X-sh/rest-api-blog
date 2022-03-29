from django.contrib import admin

from .models import Profile, Category, Post


# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        
    )