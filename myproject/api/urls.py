from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomAuthToken
from .views import UserViewSet
from .views import TestResultCreateView

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('register/', UserViewSet.as_view({'post': 'create'}), name='register'),
    path('test-results/create/', TestResultCreateView.as_view(), name='test-result-create'),
]
