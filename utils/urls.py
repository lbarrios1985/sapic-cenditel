# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^inicio/$', StartView.as_view(), name='inicio'),
    url(r'^403/$', Forbidden.as_view(), name="403error"),
]
