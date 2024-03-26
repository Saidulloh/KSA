from django.contrib import admin

from apps.our_goal.models import OurGoal


@admin.register(OurGoal)
class OurGoalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'content',
    )
