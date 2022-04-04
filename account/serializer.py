from pyexpat import model
from rest_framework import serializers
from .models import Profile, Post, Category


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields = '__all__'
        
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ='__all__' 
        
class CategorySerializers(serializers.ModelSerializer):
        model = Category
        fields = '__all__'
        
            