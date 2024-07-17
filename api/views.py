from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User, Image
from .serializers import UserSerializer, ImageSerializer
import jwt, datetime
from django.utils import timezone
import os

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
# class UserRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = "pk"

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.now() + datetime.timedelta(days=1),
            'iat': datetime.datetime.now()
        }

        user.last_login = timezone.now()
        user.save()

        token = jwt.encode(payload, os.environ.get('JWT_SECRET'), algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'id': user.id,
            'jwt': token
        }

        return response
    
class UserView(APIView):
    def get(self, request):
        print(request)
        token = request.COOKIES.get('jwt')
        token2 = request.headers.get('Cookie')
        token3 = token2.replace("jwt=", "").split(' ')
        print(token)
        print(token3[1])

        if not token3:
            raise AuthenticationFailed('Unauthenticated1')
        
        try:
            payload = jwt.decode(token, os.environ.get('JWT_SECRET'), algorithms=['HS256'])
            print(payload)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated2')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return response