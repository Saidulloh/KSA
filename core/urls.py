from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="KSA API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

api_urlpatterns = [
    # path('about_us/', include('apps.about_us.urls')),
    # path('application/', include('apps.application.urls')),
    # path('baner/', include('apps.baner.urls')),
    # path('contacts/', include('apps.contacts.urls')),
    # path('document/', include('apps.document.urls')),
    # path('gallery/', include('apps.gallery.urls')),
    # path('kyrgyz_industry/', include('apps.kyrgyz_industry.urls')),
    # path('news/', include('apps.news.urls')),
    # path('our_goal/', include('apps.our_goal.urls')),
    # path('our_worth/', include('apps.our_worth.urls')),
    # path('statistic/', include('apps.statistic.urls')),
    # path('users/', include('apps.users.urls'))
]

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # authorization
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # api
    path('', include(api_urlpatterns))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
