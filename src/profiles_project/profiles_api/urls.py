from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^hello-view/',views.HelloApiView.as_view()),
]
