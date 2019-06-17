from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from user.views import UserView

urlpatterns = [
    path('User/',UserView.as_view(),name="create"),
]
