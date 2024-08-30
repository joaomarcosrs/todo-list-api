from django.contrib.auth import authenticate, login
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
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            raise serializers.ValidationError('You must include email and password!')
        
        user = authenticate(request=self.context.get('request'), username=email, password=password)
        if not user:
            raise serializers.ValidationError('Unable to log in with credentials.')
        
        data['user'] = user
        
        return data
    