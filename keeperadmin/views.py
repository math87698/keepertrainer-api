from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, action, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from keeperadmin.models import Group, Keeper, GameStats
from keeperadmin.serializers import GroupSerializer, KeeperSerializer, GameStatsSerializer


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def api_root(request, format=None):
    return Response({
        'groups': reverse('group-list', request=request, format=format),
        'keepers': reverse('keeper-list', request=request, format=format),
        'gamestats': reverse('gamestats-list', request=request, format=format),
    })

class GroupViewSet(viewsets.ModelViewSet):
    """ 
    This viewset automatically provides 'list', 'create', 
    'retrieve', 'update' and 'destroy' of the Group Model.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class KeeperViewSet(viewsets.ModelViewSet):
    queryset = Keeper.objects.all()
    serializer_class = KeeperSerializer

    def perform_create(self, serializer):
        serializer.save()


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