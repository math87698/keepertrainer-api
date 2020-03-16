from django.contrib import admin

from .models import Group, Keeper, GameStats


admin.site.register(Group)
admin.site.register(Keeper)
admin.site.register(GameStats)