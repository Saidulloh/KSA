from rest_framework.routers import DefaultRouter

from apps.document.views import AdminDocumentApiViewSet, DocumentApiViewSet


router = DefaultRouter()
router.register(
    prefix="admin_document",
    viewset=AdminDocumentApiViewSet
)

router.register(
    prefix="document",
    viewset=DocumentApiViewSet
)

urlpatterns = router.urls
