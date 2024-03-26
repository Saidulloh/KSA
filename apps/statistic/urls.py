from rest_framework.routers import DefaultRouter

from apps.statistic.views import AdminStatisticApiViewSet, StatisticApiViewSet


router = DefaultRouter()
router.register(
    prefix="admin_statistic",
    viewset=AdminStatisticApiViewSet
)

router.register(
    prefix="statistic",
    viewset=StatisticApiViewSet
)

urlpatterns = router.urls
