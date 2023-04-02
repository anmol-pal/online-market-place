from django.contrib import admin
from django.urls import path, include
from core.views import index
from core.views import contact

#for showing images on page
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', index, name="index"),
    path('/items/', include('item.urls')),
    path('contact/',contact, name='contact' ),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
