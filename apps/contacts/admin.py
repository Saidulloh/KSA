from django.contrib import admin

from apps.contacts.models import OurContact


@admin.register(OurContact)
class OurContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
    )
