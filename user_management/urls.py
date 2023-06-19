from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
