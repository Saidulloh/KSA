from django.contrib import admin

from apps.statistic.models import Statistic


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
