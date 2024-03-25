from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAdminUser

from apps.about_us.models import AboutUs
from apps.about_us.serializers import AboutUsSerializer


class AdminAboutUsApiViewSet(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminUser]


class AboutUsApiViewSet(GenericViewSet,
                        ListModelMixin,
                        RetrieveModelMixin):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
