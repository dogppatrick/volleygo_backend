from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Gym API",
        default_version="v1",
        description="場館資料後端API",
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("v1/", include("volley_spot.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
