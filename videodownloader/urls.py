
from django.contrib import admin
from django.urls import path
from .views import video_download

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video_download/', video_download),
]
