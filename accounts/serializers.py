from rest_framework import serializers
from django.contrib.auth.models import User
from keeperadmin.models import Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    group = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all)

    class Meta:
        model = User
        fields = ['id','url','email','group']