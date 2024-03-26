from rest_framework.routers import DefaultRouter

from apps.news.views import AdminNewApiViewSet, NewApiViewSet


router = DefaultRouter()
router.register(
    prefix="admin_new",
    viewset=AdminNewApiViewSet
)

router.register(
    prefix="new",
    viewset=NewApiViewSet
)

urlpatterns = router.urls
