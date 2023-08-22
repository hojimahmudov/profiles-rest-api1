from django.urls import re_path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    re_path(r'^hello-view/', views.HelloApiView.as_view()),
    re_path(r'', include(router.urls))
]
