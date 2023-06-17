from django.shortcuts import render
from rest_framework import viewsets
from api.models import Job, Employer
from api.serializers import JobSerializers, EmpolyerSerializers


# Create your views here.

class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmpolyerSerializers

# Job viewset
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializers