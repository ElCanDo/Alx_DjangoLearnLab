from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        # Check if passwords match
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Run Django's built-in password validators
        validate_password(data['password'])
        return data

    def create(self, validated_data):
        # Remove password2 since it's not part of the model
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    


# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'bio', 'profile_picture']
#         read_only_fields = ['email', 'username', ]        

#     def get_followers_count(self, obj):
#         return obj.followers.count()

#     def get_following_count(self, obj):
#         return obj.following.count()