from rest_framework import serializers
from rest_framework.authtoken.admin import User
from ..models import *

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password','password2')

        extra_kwargs = {
            'password': {'write_only': True},
        }

    # override to save password2
    def save(self, **kwargs):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"error": "Passwords must match."})\

        email = self.validated_data['email']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "Email already registered."})

        username = self.validated_data['username']
        user = User.objects.create_user(email=email, username=username)
        user.set_password(password)
        user.save()

        return user


