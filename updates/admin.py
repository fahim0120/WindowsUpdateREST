from django.contrib import admin
from .models import Participant, Notification, Ping

admin.site.site_header = 'Admin Panel'
admin.site.site_title = 'Admin Area'
admin.site.index_title = 'Welcome to Updates Admin Panel'

# class NotificationInline(admin.TabularInline):
#     model = Notification
#     extra = 5
#
# class ParticipantAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['mturk_id']}),
#         ('Date', {'fields': ['install_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [NotificationInline]

admin.site.register(Participant)
admin.site.register(Notification)
admin.site.register(Ping)
#admin.site.register(Participant, ParticipantAdmin)