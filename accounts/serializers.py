from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import CustomUser


class AccountsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
        }
        
    def create(self, validated_data):
        name = validated_data.pop('name')
        email = validated_data['email']
        first_name, last_name = name.split(' ', 1) if ' ' in name else (name, '')
        
        user = CustomUser.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=validated_data['password']
        )
        
        token, _ = Token.objects.get_or_create(user=user)
        
        return {'token': token.key}