from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('mainApps.urls')),
    path(r'contacts/', include('mainApps.urls')),
]
