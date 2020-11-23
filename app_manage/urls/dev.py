"""hero_arithmetic_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
import time

from app_manage.views import start_scheduler, end_scheduler, health_check


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # api-auth对应授权登录url
    # path('docs/', schema_view, name='docs'),  # 配置docs的url路径
    path(r'startScheduler', start_scheduler, name='startScheduler'),
    path(r'endScheduler', end_scheduler, name='endScheduler'),
    path(r'check/healthCheck', health_check, name='healthCheck'),
]
from app_manage.views import start_scheduler, end_scheduler
end_scheduler(3)
time.sleep(1)
start_scheduler(3)