from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from keeperstats.models import GameStats
from keeperstats.serializers import GameStatsSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'gamestats': reverse('gamestats-list', request=request, format=format)
    })


class GameStatsViewSet(viewsets.ModelViewSet):
    """ 
    This viewset automatically provides 'list', 'create', 
    'retrieve', 'update' and 'destroy' of the GameStats Model.
    """
    queryset = GameStats.objects.all()
    serializer_class = GameStatsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()