from players.models import Player, Side
from django.contrib import admin

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'gender', 'age')
    list_filter = ['gender']
    search_fields = ['first_name', 'last_name']
    date_hierarchy = 'birthday'

admin.site.register(Player, PlayerAdmin)
admin.site.register(Side)
