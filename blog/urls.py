# -*- coding: utf-8 -*-



app_name="blog"
# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from church import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
   path('', views.blog_home, name='hhome'),
    path('<slug:title1>/', views.blog_detail, name='detail'),
]

