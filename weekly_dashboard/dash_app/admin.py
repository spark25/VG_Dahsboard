from django.contrib import admin
from .models import Registration, VDP, Reward_Sli, Goals_Sli
from django.contrib.auth.models import Group
# Register your models here.

class RegistrationAdmin(admin.ModelAdmin):
    fields = ['event_type', 'date_time', 'count']
    list_display = ['event_type', 'date_time', 'count']
    list_filter = ['event_type', 'date_time']
    search_fields = ['event_type', 'date_time']


class Reward_SliAdmin(admin.ModelAdmin):
    fields = ['reward', 'awarded_on', 'count']
    list_display = ['reward', 'awarded_on', 'count']


admin.site.register(Registration, RegistrationAdmin)
admin.site.register(VDP)
admin.site.register(Reward_Sli, Reward_SliAdmin)
admin.site.register(Goals_Sli)
admin.site.unregister(Group)
