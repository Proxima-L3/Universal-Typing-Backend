"""
URL configuration for typing_site_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework import routers
from test_results.views import TestResultsView


router = routers.DefaultRouter()
router.register(r'test_results_entries', TestResultsView, basename='test_results_entries')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication_app/', include('authentication.urls')),
    path('leaderboards_app', include('leaderboards.urls')),
    # path('test_results/', include('test_results.urls')),
    path('api/', include(router.urls)),
]
