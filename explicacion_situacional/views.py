from django.shortcuts import render
from django.views.generic.edit import (
    FormView, UpdateView
)
# Create your views here.
from django.contrib.gis.admin.options import OSMGeoAdmin

from .forms import ExplicacionForms


class mapquestGeoAdmin(FormView):
    form_class = ExplicacionForms
    template_name = 'map.explicacion.situacional.html'
    success_url = '/inicio/'
