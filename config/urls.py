from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="LMS API",
        default_version="v1",
        description="LMS API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="JpjGj@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("api/", include("lms.urls", namespace="lms")),
                  path("api/", include("users.urls", namespace="users")),
                  path("swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema_json"),
                  path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-_swagger_ui"),
                  path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema_redoc")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
