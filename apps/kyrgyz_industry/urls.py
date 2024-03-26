from rest_framework.routers import DefaultRouter

from apps.kyrgyz_industry.views import AdminIndustryApiViewSet, IndustryApiViewSet


router = DefaultRouter()
router.register(
    prefix="admin_industry",
    viewset=AdminIndustryApiViewSet
)

router.register(
    prefix="industry",
    viewset=IndustryApiViewSet
)

urlpatterns = router.urls
