from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAdminUser

from apps.statistic.models import Statistic
from apps.statistic.serializers import StatisticSerializer


class AdminStatisticApiViewSet(ModelViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
    permission_classes = [IsAdminUser]


class StatisticApiViewSet(GenericViewSet,
                          ListModelMixin,
                          RetrieveModelMixin):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
