from django.urls import path, include
from rest_framework.routers import DefaultRouter
from keeperadmin import views


# Create a rotuer and register our viewsets with it.
router = DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'keepers', views.KeeperViewSet)
router.register(r'gamestats', views.GameStatsViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)), 
]