# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views.caraterizacionFisicaviews import *

urlpatterns = [
                url(r'^explicacion-situacional/',
                    ExplicacionSituacionalView.as_view(),
                    name="explicacion_situacional"),
                url(r'^caracterizacion-fisica/',
                    CaracterizacionFisicaView.as_view(),
                    name="caracterizacion_fisica"),
                url(r'^ubicacion-geografica/',
                    RegisterUbicMapView.as_view(),
                    name="ubicacion_geografica"),
              ]
