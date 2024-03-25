from django.contrib import admin

from apps.baner.models import Baner


@admin.register(Baner)
class BanerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title', 
    )
