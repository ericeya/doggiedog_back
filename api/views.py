from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from .models import User, Image
from .serializers import UserSerializer, ImageSerializer
import jwt, datetime
from django.utils import timezone
import os

class RegisterView(APIView):
    def post(self, request):
        print(request.data)
        
        if request.data is not None:
            email = request.data['email']
            findEmail = User.objects.filter(email=email).first()
            if findEmail is None:
                serializer = UserSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
            else:
                raise AuthenticationFailed("Email already exists!")
        else: 
            raise AuthenticationFailed("Invalid entry. Please try again")
        
        user = User.objects.filter(email=email).first()

        print(user.id)
        payload = {
            'id': user.id,
            'exp': datetime.datetime.now() + datetime.timedelta(days=1),
            'iat': datetime.datetime.now()
        }
        # user.data.last_login = timezone.now()
        

        token = jwt.encode(payload, os.environ.get('JWT_SECRET'), algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'id': user.id,
            'jwt': token
        }

        print(response.data)

        return response
    
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
        token2 = request.headers.get('Authorization')

        if not token2:
            raise AuthenticationFailed('Unauthenticated1')
        
        try:
            payload = jwt.decode(token2, os.environ.get('JWT_SECRET'), algorithms=['HS256'])
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
    
class AllUserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        print(serializer.data)
        return Response(serializer.data)
    
class ImageListView(APIView):
    def get(self, request):
        images = Image.objects.all().select_related('user')
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
    
class UploadImageView(APIView):

    def post(self, request, *args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            raise AuthenticationFailed('Unauthenticated1')
        
        try:
            payload = jwt.decode(token, os.environ.get('JWT_SECRET'), algorithms=['HS256'])
            print(payload)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated2')
        print(request.headers)
        print(request.user)
        print(request.data)

        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=payload['id'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
