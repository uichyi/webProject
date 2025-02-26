from rest_framework import serializers
from .models import User, TestNSI, TestResult

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TestNSISerializer(serializers.ModelSerializer):
    class Meta:
        model = TestNSI
        fields = '__all__'

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'