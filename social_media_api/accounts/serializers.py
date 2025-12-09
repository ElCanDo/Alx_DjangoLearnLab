from rest_framework import serializers
from rest_framework.authtoken.models import Token

class RegistrationSerializer(serializers.ModelSerializer):
    serializer = serializers.CharField()
    token = Token.objects.all()
