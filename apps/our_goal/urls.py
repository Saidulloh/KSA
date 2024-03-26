from rest_framework.routers import DefaultRouter

from apps.our_goal.views import AdminOurGoalApiViewSet, OurGoalApiViewSet


router = DefaultRouter()
router.register(
    prefix="admin_our_goal",
    viewset=AdminOurGoalApiViewSet
)

router.register(
    prefix="our_goal",
    viewset=OurGoalApiViewSet
)

urlpatterns = router.urls
