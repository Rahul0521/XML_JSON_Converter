from django.urls import path
from .views import upload_file,error_page,download_json

urlpatterns = [
    path('', upload_file, name='upload_file'),
    path('download-json/', download_json, name='download_json'),
    path('error/', error_page, name='error_page'),
]
