"""
URL configuration for puddle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings 
from django.conf.urls.static import static 
from django.urls import path, include 
from django.contrib import admin
from core.views import index, add_sda_punjab, add_sda_haryana, add_govt_building, add_division_detail, add_railway_detail, sda_punjab_list, sda_haryana_list, govt_building_list, division_detail_list, railway_detail_list
from django.urls import path, include 

urlpatterns = [
    path('', index, name='index'),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('add-sda-punjab/', add_sda_punjab, name='add_sda_punjab'),
    path('add-sda-haryana/', add_sda_haryana, name='add_sda_haryana'),
    path('add-govt-building/', add_govt_building, name='add_govt_building'),
    path('add-division-detail/', add_division_detail, name='add_division_detail'),
    path('add-railway-detail/', add_railway_detail, name='add_railway_detail'),

    # Add missing list views
    path('sda-punjab-list/', sda_punjab_list, name='sda_punjab_list'),
    path('sda-haryana-list/', sda_haryana_list, name='sda_haryana_list'),
    path('govt-building-list/', govt_building_list, name='govt_building_list'),
    path('division-detail-list/', division_detail_list, name='division_detail_list'),
    path('railway-detail-list/', railway_detail_list, name='railway_detail_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)