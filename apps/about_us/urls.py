from rest_framework.routers import DefaultRouter

from apps.about_us.views import AdminAboutUsApiViewSet, AboutUsApiViewSet


router = DefaultRouter()
router.register(
    prefix="admin_information",
    viewset=AdminAboutUsApiViewSet
)

router.register(
    prefix="information",
    viewset=AboutUsApiViewSet
)

urlpatterns = router.urls
