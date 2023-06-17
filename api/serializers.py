from rest_framework import serializers
from api.models import Job
from api.models import Employer

# Creating Empolyer serializer
class EmpolyerSerializers(serializers.HyperlinkedModelSerializer):
    empolyer_id = serializers.ReadOnlyField()
    class Meta:
        model = Employer
        fields = '__all__'

# Creating job serializers
class JobSerializers(serializers.HyperlinkedModelSerializer):
    job_id = serializers.ReadOnlyField()
    class Meta:
        model = Job
        fields = '__all__'