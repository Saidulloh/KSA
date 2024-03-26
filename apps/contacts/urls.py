from rest_framework.routers import DefaultRouter

from apps.contacts.views import AdminOurContactApiViewSet, OurContactApiViewSet


router = DefaultRouter()
router.register(
    prefix="admin_location",
    viewset=AdminOurContactApiViewSet
)

router.register(
    prefix="location",
    viewset=OurContactApiViewSet
)

urlpatterns = router.urls
