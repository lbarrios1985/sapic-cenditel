# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^registrar-organizacion/$', RegisterOrgView.as_view(),
        name="registrar_organizacion"),
]
