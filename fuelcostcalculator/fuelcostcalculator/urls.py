from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('calculator.urls', 'calculator'), namespace='calculator')),
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    path('custom_admin/', include(('custom_admin.urls', 'custom_admin'), namespace='custom_admin')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
