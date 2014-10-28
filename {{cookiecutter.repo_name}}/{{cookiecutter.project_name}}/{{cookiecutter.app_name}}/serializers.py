from django.contrib.auth.models import User, Group
from .models import DummyModel
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class DummyModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DummyModel
        fields = ('msisdn', 'product_code', 'data')
