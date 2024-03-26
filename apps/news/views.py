from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAdminUser

from apps.news.models import New
from apps.news.serializers import NewSerializer


class AdminNewApiViewSet(ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    permission_classes = [IsAdminUser]


class NewApiViewSet(GenericViewSet,
                      ListModelMixin,
                      RetrieveModelMixin):
    queryset = New.objects.all()
    serializer_class = NewSerializer
