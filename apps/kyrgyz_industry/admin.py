from django.contrib import admin

from apps.kyrgyz_industry.models import Industry


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'description',
    )
