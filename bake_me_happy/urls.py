from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Home
    path('', include('home.urls')),

    # Products
    path('products/', include('products.urls')),

    # Basket
    path('basket/', include('basket.urls')),

    # Checkout
    path('checkout/', include('checkout.urls')),
  
# Enable serving of media files during development
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
