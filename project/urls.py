from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('our-agents', views.agents_page, name='agent'),
    path('about-us', views.about_us, name='about'),
    path('properties', views.property_page, name='properties'),
    path('property/<str:pk>', views.single_property, name='property'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)