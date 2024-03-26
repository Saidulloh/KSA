from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.baner.models import Baner
from apps.baner.serializers import BanerSerializer


class ListMixin(ListModelMixin):
    # function for getting last baner
    def list(self, request, *args, **kwargs):
        queryset = Baner.objects.all().order_by('-id')[:1]
        serializer = BanerSerializer(queryset, many=True)
        return Response(serializer.data)


class AdminBanerApiViewSet(ModelViewSet,
                           ListMixin):
    queryset = Baner.objects.all()
    serializer_class = BanerSerializer
    permission_classes = [IsAdminUser]


class BanerApiViewSet(GenericViewSet,
                      ListMixin,
                      RetrieveModelMixin):
    queryset = Baner.objects.all()
    serializer_class = BanerSerializer
