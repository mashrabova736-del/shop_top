from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shop_top import settings

urlpatterns = []

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('product.urls', namespace='product')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('contact/', include('contacts.urls', namespace='contacts')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
