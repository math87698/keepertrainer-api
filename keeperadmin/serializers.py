from rest_framework import serializers
from keeperadmin.models import Group, Keeper


class GroupSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Group
        fields = ['id', 'name', 'owner']


class KeeperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keeper
        fields = ['id','firstname','lastname','birthdate','team','group']