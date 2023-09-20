from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', index, name='index'),
    path('<str:page>/', views.no_pages, name='no_pages'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)