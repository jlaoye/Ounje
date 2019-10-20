"""foodtasker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
from ounjeapp import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView # new
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),

    #path('/merchant/sign-in', views.merchant_signin,
    #    name = 'merchant_signin'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('merchant/', views.merchant_home,
        name ='merchant_home'),
#    path('', views.merchant_home, name='merchant_home'),
     path('signup/', views.restaurant_signUp, name='restaurant_signUp'),
        #name ='merchant_logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
