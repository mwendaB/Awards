from rest_framework import serializers
from .models import Profile,Projects

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'photo', 'user')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'description', 'shot','url','user')