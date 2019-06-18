from django.shortcuts import render,get_list_or_404, get_object_or_404
from .forms import CreateUserForm
from .serializers import UsersSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.generics import GenericAPIView,CreateAPIView,RetrieveUpdateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
class GetView(ListAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    def get(self, request, pk):
        user = User.objects.filter(userId=pk,status=1)
        serializer = UsersSerializer(user, many=True)
        return Response({"user": serializer.data})
    def delete(self,request,pk):
        user = User.objects.get(userId=pk)
        user.status=0
        user.save()
        serializer = UsersSerializer(user, many=True)
class PostView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer