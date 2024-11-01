# main/urls.py

from rest_framework.routers import DefaultRouter
from .api_views import PostViewSet, CommentViewSet, LikeViewSet,UserViewSet, login_view, logout_view
from django.urls import path, include
from . import api_views
from . import views

# REST API reititys
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'users', UserViewSet)
    
# URLS
urlpatterns = [
    # REST API reitit
    path('api/', include(router.urls)),
    path('api/login/', login_view, name='api_login'),
    path('api/logout/', logout_view, name='api_logout'),
    path('profile/', api_views.user_profile_view, name='user-profile'),
    #feed
    path('', views.feed, name='feed'),
]

#ok