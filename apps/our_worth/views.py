from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAdminUser

from apps.our_worth.models import OurWorth
from apps.our_worth.serializers import OurWorthSerializer


class AdminOurWorthApiViewSet(ModelViewSet):
    queryset = OurWorth.objects.all()
    serializer_class = OurWorthSerializer
    permission_classes = [IsAdminUser]


class OurWorthApiViewSet(GenericViewSet,
                         ListModelMixin,
                         RetrieveModelMixin):
    queryset = OurWorth.objects.all()
    serializer_class = OurWorthSerializer
