
from django.contrib.auth import authenticate, get_user_model

from rest_framework.views import APIView
from rest_framework.response  import Response
from rest_framework import permissions, generics

from .permissions import AnonPermission

from rest_framework_jwt.settings import api_settings

from django.db.models import Q

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

from .serializers import UserRegisterSerializer


User =get_user_model()

class AuthView(APIView):
    
    permission_classes     = [permissions.AllowAny]
    
    def post(self,request, *args, **kwargs):
        print(request.user)
        
        data = request.data
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(username=username, password=password)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        response = jwt_response_payload_handler(token,user, request=request)
        return Response(response)

class RegisterAPIView(generics.CreateAPIView):
    queryset            = User.objects.all()
    serializer_class    = UserRegisterSerializer
    permission_classes  = [AnonPermission]
    
    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
    
    
    
'''
class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data        = request.data
        username    = data.get('username')
        email       = data.get('email')
        password    = data.get('password')
        password2   = data.get('password2')
        
        qs = User.objects.filter(
            Q(username__iexact=username) |
            Q(email__iexact=username)
        ).distinct()
        
        if password != password2:
            return Response({"password": "password must match"}, status=401)
        
        if qs.exists():
            return Response({"password": "Password must match"}, status=401)
        else:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response = jwt_response_payload_handler(token,user, request=request)
            return Response(response)

        '''    
        