"""rmics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Index
from django.conf.urls.static import static 
from django.conf import settings
import notifications.urls


urlpatterns = [
    path('', include('user.urls')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('admin/', admin.site.urls),
    path('ams/', include('ams.urls')),
    path('drms/', include('drms.urls')),
    path('cfms/', include('cfms.urls')),
    path('notis/', include('notis.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
