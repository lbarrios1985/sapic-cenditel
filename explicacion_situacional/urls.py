# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import *

urlpatterns = [
                url(r'^explicacion-situacional/', mapquestGeoAdmin.as_view(), name="explicacion_situacional"),
              ]
