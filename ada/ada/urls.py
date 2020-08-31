from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ada_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/apps/', include(('ada_app.api.urls', 'api'), namespace='api'))
]
