from rest_framework import serializers
from rest_framework.authtoken.models import Token

class RegistrationSerializer(serializers.ModelSerializer):
    serializer = serializers.CharField()
    token = Token.objects.create()

    user = get_user_model().objects.create_user
