from rest_framework import serializers
from django.contrib.auth.models import User
from web.models import Placeholder


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

