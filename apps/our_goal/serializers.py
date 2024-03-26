from rest_framework import serializers

from apps.our_goal.models import OurGoal


class OurGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurGoal
        fields = '__all__'
