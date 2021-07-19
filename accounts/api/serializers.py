from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from django.utils import timezone
import datetime
from django.conf import settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

expires_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']

User = get_user_model()

class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =[
            'id',
            'username',
        ]

class UserRegisterSerializer(serializers.ModelSerializer):
    password        = serializers.CharField(style={'input_type':'password'}, write_only=True)
    password2       = serializers.CharField(style={'input_type':'password'}, write_only=True)
    token           = serializers.SerializerMethodField(read_only=True)
    expires         = serializers.SerializerMethodField(read_only=True)
    token_response  = serializers.SerializerMethodField(read_only=True)
    message         = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'password2',
            'token',
            'expires',
            'token_response',
            'message',
        ]
        extra_kwargs = {'password': {'write_only': True}}
    
    def get_message(self, obj):
        return "Thank you for registering with us"
    
    def get_token_response(self,obj):
        user = obj
        payload = jwt_payload_handler(user)
        token   = jwt_encode_handler(payload)
        context = self.context
        request = context['request']
        response = jwt_response_payload_handler(token,user, request=request)
        return response
        
    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if(qs.exists()):
            raise serializers.ValidationError("User with this username already exist")
        return value
    
    def validate_email(self,value):
        qs = User.objects.filter(email__iexact=value)
        if(qs.exists()):
            raise serializers.ValidationError('Email with this email address alredy exist')
        return value
        
        
    def validate(self,data):
        pw1 = data.get('password')
        pw2 = data.pop('password2')
        
        if pw1 != pw2:
            raise serializers.ValidationError("password must match1")
        return data
    
    def get_token(self, obj):
        user    = obj
        payload = jwt_payload_handler(user)
        token   = jwt_encode_handler(payload)
        print(token)
        return token
    
    def get_expires(self, obj):
        expires = timezone.now() + expires_delta - datetime.timedelta(seconds=200)
        return expires
    
    def create(self,validated_data):
        print(validated_data)
        user_obj = User(
            username=validated_data.get('username'),
            email = validated_data.get('email')
            )
        user_obj.set_password((validated_data.get('password')))
        user_obj.save()
        print(user_obj)
        return user_obj
    
    
    
        
