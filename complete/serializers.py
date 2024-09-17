from rest_framework import serializers
from .models import Complete


class CompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complete
        fields = ('id', 'start', 'body', 'complete_timestamp')