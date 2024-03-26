from rest_framework import serializers

from apps.our_worth.models import OurWorth


class OurWorthSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurWorth
        fields = '__all__'
