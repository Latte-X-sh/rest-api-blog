from tkinter.ttk import Style
from django.contrib.auth.models import  User

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
        lookup_field = 'post_url_slug'
        
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__' 

class RegistrationSerializer(serializers.ModelSerializer):
    password_match = serializers.CharField(style={'input_type' : 'password'}, write_only = True )
    class Meta:
        model = User
        fields = ['email','username','password','password_match']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    def save(self):
        user_account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password_match = self.validated_data['password_match']
        if password == password_match:
            user_account.set_password(password)
            user_account.save()
            return user_account
        else:
            raise serializers.ValidationError({'password':"Passwords don't match"})
            