# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from church import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('curriculum/', views.curriculum, name='curriculum'),
   path('admission/', views.admission, name='admission'),
   path('contact/', views.contact, name='contact'),
   path('facility/', views.facility, name='facility'),
   path('gallery/', views.gallery, name='gallery'),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)