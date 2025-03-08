from django.urls import path, include
from rest_framework.routers import DefaultRouter
from psychoTests.backend.views import UserViewSet, TestNSIViewSet, TestResultViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tests', TestNSIViewSet)
router.register(r'test-results', TestResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]