from django.contrib import admin
from .models import Capabilities, User


class CapabilitiesAdmin(admin.ModelAdmin):
    list_display = ('Username',)

    def user(self, obj):
        try:
            return obj.user
        except User.DoesNotExist:
            return "User does not exist"

    user.short_description = 'User'


admin.site.register(Capabilities, CapabilitiesAdmin)