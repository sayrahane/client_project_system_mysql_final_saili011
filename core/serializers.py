from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    user_ids = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, write_only=True, required=False
    )

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'user_ids', 'created_at', 'created_by']
        read_only_fields = ['id', 'created_at', 'created_by']

    def create(self, validated_data):
        user_ids = validated_data.pop("user_ids", [])
        project = Project.objects.create(**validated_data)
        project.users.set(user_ids)
        return project

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects', 'created_at', 'updated_at', 'created_by']
