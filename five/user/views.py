from django.shortcuts import render
from .forms import CreateUserForm
from .serializers import UsersSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.views import APIView
# Create your views here.
# def createUser(request):
# 	if request.method=='POST':
# 		form=CreateUserForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 	else:
# 		form=CreateUserForm()
# 	return render(request, 'create.html', {'form': form})

class UserView(APIView):
    def post(self, request):
        user = request.data.get('user')

        # Create an article from the above data
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.title)})
    def get(self, request):
        user = User.objects.all()
        serializer = UsersSerializer(user, many=True)
        return Response({"user": serializer.data})