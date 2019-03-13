"""gptetlt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static

from tlt import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^purchases/$', views.purchases, name='purchases'),
    url(r'^debt/$', views.debt, name='debt'),
    url(r'^conctacts/$', views.conctacts, name='conctacts'),
    url(r'^tariff/$', views.tariff, name='tariff'),
    url(r'^information/$', views.information, name='information'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
