from rest_framework import serializers
from .models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("userId","first_name", "last_name")

    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     instance.userId = validated_data.get('userId', instance.userId)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
     
    #     instance.save()
    #     return instance