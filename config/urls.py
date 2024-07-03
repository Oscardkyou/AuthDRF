from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Authentication API",
      default_version='v1',
      description="API for Authentication application",
      terms_of_service="https://www.example.com/policies/terms/",
      contact=openapi.Contact(email="contact@neotour.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('lorby/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('lorby/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("lorby/admin/", admin.site.urls),
    path('lorby/', include('my_auth.urls'))
]
