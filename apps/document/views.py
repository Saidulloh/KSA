from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAdminUser

from apps.document.models import Document
from apps.document.serializers import DocumentSerializer


class AdminDocumentApiViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAdminUser]


class DocumentApiViewSet(GenericViewSet,
                         ListModelMixin,
                         RetrieveModelMixin):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
