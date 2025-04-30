from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('chambres/', include('chambres.urls')),
    path('reservations/', include('reservations.urls')),
    path('materiels/', include('materiels.urls')),
    path('etages/', include('etages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 