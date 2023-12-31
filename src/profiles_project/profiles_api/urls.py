from django.urls import re_path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, basename='login')
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    re_path(r'^hello-view/', views.HelloApiView.as_view()),
    re_path(r'', include(router.urls))
]
