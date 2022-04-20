from pickle import FALSE
from tkinter import CASCADE
from django.conf import settings

from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
# The profile model - Extension of the user model
#This is the category for our blogs  
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    
    def __str__(self) -> str:
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User,related_name="user", on_delete=models.CASCADE)
    profile_pictue = models.ImageField(default="default.jpg", upload_to="profile_pictures")
    bio = models.TextField()
    category = models.ManyToManyField(Category,blank=True)
    
    def __str__(self) -> str:
        return self.user.username

    def get_catgeory(self):
        return ", ".join([p.name for p in self.category.all()])
    



class Post(models.Model):
    class Meta:
        ordering = ["post_published_date"]
        
    
    post_title =  models.CharField(max_length=100,unique=True)
    post_sb_title = models.CharField(max_length=100,blank=True)
    post_url_slug= models.SlugField(max_length=100,unique=True)
    post_body = models.TextField()
    post_meta_description = models.TextField(max_length=100,blank=True)
    post_date_created = models.DateTimeField(auto_now_add=True)
    post_modified = models.DateTimeField(auto_now=True)
    post_published_date = models.DateTimeField(blank=True,null=True)
    post_published_status =  models.BooleanField(default=False)
    post_author =  models.ForeignKey(User,related_name="author_name",on_delete=models.PROTECT)
    post_category = models.ManyToManyField(Category,blank=True)
    
    def __str__(self) -> str:
        return self.post_title

    def get_post_catgeory(self):
         return ", ".join([p.name for p in self.post_category.all()])

    def post_status_to_true(self):
        if self.post_published_status is False:
            self.post_published_status=True
        else:
            self.post_published_status 

    def clean(self):
        self.post_status_to_true()
        super().clean()
    
    def save(self,*args,**kwargs):
        self.clean()
        super(Post,self).save(*args,**kwargs)

    
    
    
    
  
        