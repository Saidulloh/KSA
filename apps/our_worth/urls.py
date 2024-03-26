from rest_framework.routers import DefaultRouter

from apps.our_worth.views import AdminOurWorthApiViewSet, OurWorthApiViewSet


router = DefaultRouter()
router.register(
    prefix="admin_our_worth",
    viewset=AdminOurWorthApiViewSet
)

router.register(
    prefix="our_worth",
    viewset=OurWorthApiViewSet
)

urlpatterns = router.urls
