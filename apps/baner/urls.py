from rest_framework.routers import DefaultRouter

from apps.baner.views import AdminBanerApiViewSet, BanerApiViewSet


router = DefaultRouter()
router.register(
    prefix="admin_baner",
    viewset=AdminBanerApiViewSet
)

router.register(
    prefix="baner",
    viewset=BanerApiViewSet
)

urlpatterns = router.urls
