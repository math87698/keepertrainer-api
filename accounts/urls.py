from django.urls import path
from rest_framework import renderers
from rest_framework.authtoken import views as rest_framework_views
from accounts import views
from accounts.views import UserViewSet, api_root

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', api_root),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    #path('login/', views.get_auth_token, name='login'),
    #path('logout/', views.logout_user, name='logout'),
    #path('auth/', views.login_form, name='login_form'),
    path('get_auth_token/', rest_framework_views.obtain_auth_token, name='get_auth_token')
]