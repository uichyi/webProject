from django.urls import path
from .views import index, login_user, register_user, save_test_result


urlpatterns = [
    path('', index),
    path('login/', login_user, name='login_user'),
    path('register/', register_user, name='register_user'),
    path('test-results/create/', save_test_result, name='test-result-create'),
]
