
from rest_framework import serializers

from .models import NetworkCoveragePoint


class NetworkCoverageSerializer(serializers.ModelSerializer):

    class Meta:
        model = NetworkCoveragePoint
        fields = ['operator', 'networks']
