from rest_framework.routers import DefaultRouter

from apps.gallery.views import AdminGalleryApiViewSet, GalleryApiViewSet


router = DefaultRouter()
router.register(
    prefix="admin_gallery",
    viewset=AdminGalleryApiViewSet
)

router.register(
    prefix="gallery",
    viewset=GalleryApiViewSet
)

urlpatterns = router.urls
