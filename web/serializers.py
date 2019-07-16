from rest_framework import serializers
from django.contrib.auth.models import User
from web.models import Placeholder, Officer, Incident


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class PlaceholderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Placeholder
        fields = ('placeholder',)

    def create(self, validated_data):
        return Placeholder.objects.create(**validated_data)


class OfficerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Officer
        fields = ('available', 'location_x', 'location_y')

        def create(self, validated_data):
            return Officer.objects.create(**validated_data)


class IncidentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Incident
        fields = ('officer', 'location_x', 'location_y', 'type')

        def create(self, validated_data):
            return Incident.objects.create(**validated_data)

