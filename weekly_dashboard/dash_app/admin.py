from django.contrib import admin
from .models import Registration, Reward_Sli, Goals_Sli, Registration_KR, Reward_KR, Goals_KR, VDP_Sli_KR
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

class Reward_KRAdmin(admin.ModelAdmin):
    fields = ['reward', 'awarded_on', 'count']
    list_display = ['reward', 'awarded_on', 'count']

admin.site.register(Registration, RegistrationAdmin)
admin.site.register(VDP_Sli_KR)
admin.site.register(Reward_Sli, Reward_SliAdmin)
admin.site.register(Goals_Sli)
admin.site.register(Registration_KR)
admin.site.register(Reward_KR,Reward_KRAdmin)
admin.site.register(Goals_KR)
admin.site.unregister(Group)
