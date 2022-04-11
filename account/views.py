from unicodedata import lookup
from account.models import Post, Profile
from account.serializer import ProfileSerializers, PostSerializers

from rest_framework import viewsets

# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class =  PostSerializers
    lookup_field = 'post_url_slug'

class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    
    