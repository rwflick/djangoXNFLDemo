from django.contrib import admin
from nfl.models import Team, Player

# Register your models here.
class CustomTeamAdmin(admin.ModelAdmin):
    list_display = ['location', 'nickname', 'conference', 'division']

admin.site.register(Team, CustomTeamAdmin)

class CustomPlayerAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'position', 'team']

admin.site.register(Player, CustomPlayerAdmin)
