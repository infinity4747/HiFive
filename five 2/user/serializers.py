from rest_framework import serializers
from .models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("userId","first_name", "last_name")
