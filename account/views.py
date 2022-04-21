from argparse import Action

from attr import dataclass
from account.models import Post, Profile
from account.serializer import ProfileSerializers, PostSerializers, RegistrationSerializer  
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class =  PostSerializers
    lookup_field = 'post_url_slug'

class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    
class UsersRegistrationViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer 

    # @action(detail=False, methods=['POST'])
    # def register(self,request):
    #     serializer =  RegistrationSerializer(data=request.data)
    #     data = {}
    #     if serializer.is_valid(self):
    #         account = serializer.save()
    #         data['reponse'] = "Successfuly registered a new user"
    #         data['email'] = account.email
    #         data['username'] = account.username
    #     else:
    #         data = serializer.errors
    #     return Response(data)
