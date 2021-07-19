from rest_framework import serializers
from status.models import Status

from accounts.api.serializers import UserPublicSerializer

class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
    email  = serializers.EmailField()
    

class StatusSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    class Meta:
        model = Status
        fields =[
            'id',
            'user',
            'content',
            'image'           
        ]
        read_only_fields =['user']
    
    def validate_content(self, value):
        if len(value) > 100:
            raise serializers.ValidationError("This is way too long.")
        return value
    
    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("content or image is required")
        return data
    
        
        