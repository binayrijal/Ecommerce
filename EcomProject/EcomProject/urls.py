
from django.contrib import admin
from django.urls import path,include
from startecom.views import index,contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('startecom.urls')),
    path('inbox/',include('communication.urls'),name="communication"),
    path('items/',include('items.urls')),
    path('dashboard/',include('dashboard.urls'),name="dashboard"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
