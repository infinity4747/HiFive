from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from user.views import GetView,PostView

urlpatterns = [
 	path('create/',PostView.as_view(),name="create"),
    path('<int:pk>',GetView.as_view(),name="get"),
   
]
