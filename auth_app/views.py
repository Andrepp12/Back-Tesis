from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Agregar roles al token
        token['role'] = user.role
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['role'] = self.user.role  # Devolver también el rol en la respuesta
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CreateUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Obtiene los datos de la solicitud
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        role = request.data.get('role', 'vendedor')  # Rol por defecto 'vendedor' si no se especifica

        # Verifica que los campos obligatorios estén presentes
        if not username or not email or not password or not role:
            return Response({"error": "Por favor, proporciona todos los campos requeridos."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Crea el nuevo usuario
        user = CustomUser.objects.create(
            username=username,
            email=email,
            password=make_password(password),  # Encripta la contraseña
            role=role  # Asigna el rol especificado
        )

        # Devuelve la respuesta de éxito
        return Response({
            "message": "Usuario creado exitosamente.",
            "username": user.username,
            "email": user.email,
            "role": user.role
        }, status=status.HTTP_201_CREATED)