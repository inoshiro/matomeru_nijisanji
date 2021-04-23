from django.contrib import admin

from .models import Liver


class LiverAdmin(admin.ModelAdmin):
    list_display = ('name', 'ruby', 'slug', 'created_at', 'updated_at')


admin.site.register(Liver, LiverAdmin)
