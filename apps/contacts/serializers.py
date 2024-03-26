from rest_framework import serializers

from apps.contacts.models import OurContact


class OurContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurContact
        fields = '__all__'
