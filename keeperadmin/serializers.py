from rest_framework import serializers
from keeperadmin.models import Group, Keeper, GameStats


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


class GameStatsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='gamestats-detail', format='html')

    class Meta:
        model = GameStats
        fields = ['id', 'recording_date', 'keeper', 'minutes_played', 'goals_against', 'shots_on_goal', 'saves',
        'total_passes', 'passes_right', 'passes_left', 'passes_successfull']