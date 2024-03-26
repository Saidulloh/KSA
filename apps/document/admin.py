from django.contrib import admin

from apps.document.models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )
