from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAdminUser

from apps.kyrgyz_industry.models import Industry
from apps.kyrgyz_industry.serializers import IndustrySerializer


class AdminIndustryApiViewSet(ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = [IsAdminUser]


class IndustryApiViewSet(GenericViewSet,
                         ListModelMixin,
                         RetrieveModelMixin):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
