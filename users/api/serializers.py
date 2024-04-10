from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_repeat = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'password_repeat',
        ]

    def validate(self, data: dict[str, str]) -> dict[str, str]:
        password_repeat = data.pop("password_repeat")
        password = data['password']
        if password != password_repeat:
            raise serializers.ValidationError("password not matched")
        data['password'] = make_password(password)
        return data
    
