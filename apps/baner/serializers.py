from rest_framework import serializers

from apps.baner.models import Baner


class BanerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baner
        fields = '__all__'
