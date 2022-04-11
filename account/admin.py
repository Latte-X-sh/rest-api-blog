from django.contrib import admin

from .models import Profile, Category, Post


# Register your models here.




@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model= Profile
    list_display=("id","user","bio","get_catgeory")
    search_fields =("user__username","id",)

    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model= Category
    list_display=("id","name")
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model=Post
    list_display=("id","get_post_catgeory","post_title","post_sb_title","post_author","post_published_status","post_date_created","post_published_date",)
    list_filter=("post_author","post_category","post_published_date")
    list_editable=("post_title","post_sb_title",)
    search_fields = ("post_title","post_sb_title","post_url_slug")
    prepopulated_fields={
        "post_url_slug":(
            "post_title","post_sb_title"
        ),
     
    }
    save_on_top =True
    
        

