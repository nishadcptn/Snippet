from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class UserSerialier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SnippeteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        exclude =('user','tag')


class AllSnippeteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'

        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'