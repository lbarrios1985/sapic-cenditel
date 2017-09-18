# -*- coding: utf-8 -*-
"""
SAPIC

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida - https://planificacion.cenditel.gob.ve/trac/wiki/WikiStart#a5.-SistemaAutomatizadodePlanificaciónIntegralComunalSAPIC
"""
## @package explicacion_situacional.views
#
# Vistas correspondientes a la explicacion situacional
# @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0

from django.contrib import messages
from django.shortcuts import render
from django.views.generic.edit import (
    FormView, UpdateView
)
# Create your views here.
from django.contrib.gis.admin.options import OSMGeoAdmin

from .forms import ExplicacionForms


class RegisterExplSitView(FormView):
    """!
    Clase que controla el formulario en la vista de la explicacion situacional

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 18-09-2017
    @version 1.0.0
    """
    form_class = ExplicacionForms
    template_name = 'map.explicacion.situacional.html'
    success_url = '/inicio/'

    def form_valid(self, form, **kwargs):
        """
        Funcion que valida el formulario de registro de la explicacion situacional
        @return: Dirige con un mensaje de exito a el home
        """
        form.save()
        messages.success(self.request, "Explicacion situacional, \
                                        registrada con exito")
        return super(RegisterExplSitView, self).form_valid(form)
