# System
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Project
from config.settings.swagger.setup import SwaggerSetup
from core.view import HealthCheckView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("apis/v1/users/", include("apis.users.urls")),
    path("health-check", view=HealthCheckView.as_view(), name="health_check"),
]

# Swagger
urlpatterns = SwaggerSetup.do_urls(urlpatterns=urlpatterns)

# Static/Media File Root (CSS, JavaScript, Images)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
