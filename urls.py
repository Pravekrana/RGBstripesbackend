from django.contrib import admin
from django.urls import path, include
from color_identification.views import process_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('process_image/', process_image, name='process_image'),
    # Add other URLs as needed
]
