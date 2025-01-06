from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = '__all__'

    def get_followers_count(self, obj):
        return obj.followers.count()

    class RegisterSerializer(serializers.ModelSerializer):
        token = serializers.CharField(read_only=True)
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'bio', 'profile_picture', 'token']

        def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email = validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', None),
            profile_picture=validated_data.get('profile_picture', None)
        )

        Token.objects.create(user=user)
        return user
        
    class LoginSerializers(serializers.ModelSerializer):
        username = serializers.CharField()
        password = serializers.CharField()

    class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = CustomUser
            fields = ['username', 'email', 'bio', 'profile_picture', 'followers']
            read_only_fields = ['username', 'followers']  # Users cannot change these fields