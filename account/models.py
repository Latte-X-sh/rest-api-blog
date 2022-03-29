from django.conf import settings

from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField


# Specifying tag choices
# it can be any iterable obj - not restricted to
# tuples and dictionaries etc
#tuple of tuples
tag_choices =(
    ('ENG','Engineering'),
    ('CS','Computing'),
    ('HT','Health'),    
    ('BS','Business'),
    ('ST','Sports'),
    ('OT','Other'),
)

# Create your models here.
# The profile model - Extension of the user model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    profile_pictue = models.ImageField(default="default.jpg", upload_to="profile_pictures")
    bio = models.TextField()
    category = MultiSelectField(max_length=100,max_choices = len(tag_choices), choices=tag_choices)
    
    def __str__(self) -> str:
        return self.user.username
    

#This is the category for our blogs  
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True,choices=tag_choices)
    
    def __str__(self) -> str:
        return self.name
    

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
    post_author =  models.ForeignKey(User, on_delete=models.PROTECT)
    post_category = models.ManyToManyField(Category,default='Random')
    
    