# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import *
from .ajax import *

urlpatterns = [
    url(r'^registrar-organizacion/$', RegisterOrgView.as_view(),
        name="registrar_organizacion"),
    url(r'^listar-organizacion/$', ListOrgView,
        name="listar_organizacion"),
    # Ajax list Organizaciones, for Administradores
    url(r'^listar-organizaciones/$', ListOrgsAjaxView.as_view(),
        name="listar_orgs"),
       
]
