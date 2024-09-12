from django.urls import path
from .views import test_upload

urlpatterns = [
    path('test_upload/', test_upload, name='test_upload'),
]
