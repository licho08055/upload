from django.urls import path
from .views import book_upload,book_download,Load

urlpatterns = [
    path('', book_upload, name='book'),
    path('load/', book_download, name='load'),
    path('loads/', Load.as_view(), name='loads')
]