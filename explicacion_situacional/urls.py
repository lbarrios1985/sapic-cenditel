# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views.caracterizacionFisicaView import *
from .views.genericEncuestasView import *
from .ajax import *

urlpatterns = [
                url(r'^explicacion-situacional/',
                    ExplicacionSituacionalView.as_view(),
                    name="explicacion_situacional"),
                url(r'^caracterizacion-fisica/$',
                    CaracterizacionFisicaView.as_view(),
                    name="caracterizacion_fisica"),
                url(r'^ubicacion-geografica/',
                    RegisterUbicMapView.as_view(),
                    name="ubicacion_geografica"),
                url(r'^caracterizacion-fisica/condicion-suelos/(?P<pk>25+)$',
                    EncuestasParticiparView.as_view(),
                    name="condicion_suelos"),
                # Ajax
                url(r'^validar-participacion-ajax',
                    validar_participacion,
                    name="validar_participacion_ajax"),
              ]
