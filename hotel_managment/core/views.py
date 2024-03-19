from django.contrib.auth import (
    authenticate, login, logout
)
from rest_framework.response import Response
from rest_framework.views import APIView, Http404
from rest_framework import status

from core.models import Hotel, User
from core.serializers import HotelSerializer, UserSerializer
from core.utils import get_tokens_for_user
from core.permissions import (
    ClientPermission,
    FunctionaryPermission,
    AdminPermission
)

# Create your views here.

class UserList(APIView):
    permission_classes = (FunctionaryPermission,)

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class LoginView(APIView):
    def post(self, request, format=None):
        if ('email' not in request.data) or (
            'password' not in request.data
        ):
            return Response(
                {'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST
            )
        email, password = request.POST['email'], request.POST['password']
        user = authenticate(
            request, email=email, password=password
        )
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response(
                {'msg': 'Login success.', **auth_data},
                status=status.HTTP_200_OK
            )
        return Response(
            {'msg': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED
        )

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(
            {'msg': 'Successfully logged out'},
            status=status.HTTP_200_OK
        )

class HotelList(APIView):
    permission_classes = (FunctionaryPermission,)

    def get(self, request, format=None):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class HotelDetail(APIView):
    permission_classes = (FunctionaryPermission,)

    def get_obj(self, pk):
        try:
            return Hotel.objects.get(uuid=pk)
        except Exception:
            raise Http404

    def get(self, request, pk, format=None):
        hotel = self.get_obj(pk)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        hotel = self.get_obj(pk)
        serializer = HotelSerializer(hotel, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        hotel = self.get_obj(pk)
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

