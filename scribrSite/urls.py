# scribrSite/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('upload/', include('upload.urls')),  # Adjust 'myapp' to the actual name of your app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
