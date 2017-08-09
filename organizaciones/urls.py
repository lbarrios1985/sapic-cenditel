# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import *

from .utils import obtenerOrganizaciones

urlpatterns = [
    url(r'^registrar-organizacion/$', RegisterOrgView.as_view(),
        name="registrar_organizacion"),
    url(r'^organizaciones_sociales/$', obtenerOrganizaciones, name='obtener_orgs'),
]
