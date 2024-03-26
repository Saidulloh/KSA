from rest_framework import serializers

from apps.kyrgyz_industry.models import Industry


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'
