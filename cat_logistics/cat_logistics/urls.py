from django.contrib import admin
from django.urls import include, path

handler404 = 'pages.views.page_not_found'

handler500 = 'pages.views.server_error'

urlpatterns = [
    path('', include('catalog.urls')),
    path('admin/', admin.site.urls),
]
