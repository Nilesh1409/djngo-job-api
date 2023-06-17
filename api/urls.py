
from django.urls import path, include
from rest_framework import routers
from api.views import JobViewSet, EmployerViewSet

router = routers.DefaultRouter()
router.register(r'jobs',JobViewSet)
router.register(r'empolyers', EmployerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
