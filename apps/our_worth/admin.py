from django.contrib import admin

from apps.our_worth.models import OurWorth


@admin.register(OurWorth)
class OurWorthAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
