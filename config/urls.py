from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manufacturers_and_retailers.urls')),
    path('users/', include('users.urls')),
]
