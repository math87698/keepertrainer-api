from rest_framework import serializers
from keeperstats.models import GameStats


class GameStatsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='gamestats-detail', format='html')

    class Meta:
        model = GameStats
        fields = ['id', 'recording_date', 'keeper', 'minutes_played', 'goals_against', 'shots_on_goal', 'saves',
        'total_passes', 'passes_right', 'passes_left', 'passes_successfull']