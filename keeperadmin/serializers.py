from rest_framework import serializers
from keeperadmin.models import Group, Keeper


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.HyperlinkedIdentityField(view_name='group-detail', format='html')

    class Meta:
        model = Group
        fields = ['id', 'name', 'owner']


class KeeperSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='keeper-detail', format='html')

    class Meta:
        model = Keeper
        fields = ['id','firstname','lastname','birthdate','team','group']