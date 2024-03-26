from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAdminUser

from apps.contacts.models import OurContact
from apps.contacts.serializers import OurContactSerializer


class AdminOurContactApiViewSet(ModelViewSet):
    queryset = OurContact.objects.all()
    serializer_class = OurContactSerializer
    permission_classes = [IsAdminUser]


class OurContactApiViewSet(GenericViewSet,
                           ListModelMixin,
                           RetrieveModelMixin):
    queryset = OurContact.objects.all()
    serializer_class = OurContactSerializer
