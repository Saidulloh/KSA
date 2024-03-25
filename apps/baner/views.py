from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAdminUser

from apps.baner.models import Baner
from apps.baner.serializers import BanerSerializer


class AdminBanerApiViewSet(ModelViewSet):
    queryset = Baner.objects.all()
    serializer_class = BanerSerializer
    permission_classes = [IsAdminUser]


class BanerApiViewSet(GenericViewSet,
                           ListModelMixin,
                           RetrieveModelMixin):
    queryset = Baner.objects.all()
    serializer_class = BanerSerializer
