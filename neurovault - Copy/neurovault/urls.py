from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("security.urls")),   # 👈 THIS IS REQUIRED
    path("admin/", admin.site.urls),
]
