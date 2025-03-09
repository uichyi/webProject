from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import User, TestNSI, TestResult
from .serializers import LoginSerializer, UserSerializer, TestNSISerializer, TestResultSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TestResult
from .serializers import TestResultSerializer
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def index(request):
    return render(request, 'index.html')


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def save_test_result(request):
    if request.method == 'POST':
        request.data['accuracy'] = round(request.data['accuracy'], 2)
        print(request.data)
        serializer = TestResultSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.shortcuts import render
from django.template import RequestContext

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)

            if user.check_password(raw_password=password):
                return Response({'message': 'Вход выполнен успешно', 'user_id': user.id})
            else:
                return Response({'error': 'Неверный пароль'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)