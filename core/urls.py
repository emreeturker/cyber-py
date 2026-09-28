from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('_nested_admin/', include('nested_admin.urls')),
    path('admin/', admin.site.urls),
    path("attacks/", include("attacks.urls")),
    path("tools/", include("tools.urls")),
    path("linux_commands/", include("linux_commands.urls")),
    path("ports/", include("ports.urls")),
    path("", views.home, name="home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)