from core.models import Hotel, User
from rest_framework import serializers
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenSerializer(TokenObtainPairView):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['admin'] = user.is_superuser
        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_fields = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']

        if not password:
            raise serializers.ValidationError({'password': 'Password must be seted'})

        user = User(email=email)
        user.set_password(password)
        user.save()
        return user

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('uuid', 'name',)
    
    def create(self, validated_data):
        name = validated_data['name']
        hotel = Hotel(name=name)
        hotel.save()
        return hotel
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
