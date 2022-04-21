from xml.etree.ElementInclude import include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account import views

router =  DefaultRouter()
router.register(r'account',views.UsersRegistrationViewset,basename='account')
router.register(r'posts', views.PostViewset, basename ="posts")
router.register(r'profile',views.ProfileViewset, basename ="profile")
urlpatterns = [
    path('',include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
