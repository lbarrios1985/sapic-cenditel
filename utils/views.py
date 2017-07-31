# -*- encoding: utf-8 -*-
"""!
Vista que controla los procesos de las utilidades de la pltaforma

@author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
@copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
@date 29-05-2017
@version 1.0.0
"""
import json
from django.contrib import messages
from django.contrib.auth.mixins import (
    PermissionRequiredMixin, LoginRequiredMixin
)
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import (
    redirect, render
)
from django.views.generic import TemplateView
from braces.views import GroupRequiredMixin

from .models import *


def obtenerEstados():
    """
    Función que permite obtener la lista de estados

    El método hace una lista consultando el modelo Estado

    @return: Lista de estados
    """
    try:

        if Estado.objects.exists():
            consulta = Estado.objects.all().values('id', 'nombre')
        else:
            consulta = [{'id': '', 'nombre': ''}]
    except:
        consulta = [{'id': '', 'nombre': ''}]

    return consulta

def obtenerMunicipios(request):
    """
    Función que permite obtener la lista de municipios asociados a un estado

    El método hace un llamado al modelo para realizar una consulta

    @param id_estado: Identificador del estado
    @type id_estado: entero

    @return: Lista de municipios asociados al estado
    """
    try:
        if Municipio.objects.exists():
            id_estado = request.GET.get('id_estado')
            municipios = Municipio.objects.filter(estado_id=id_estado).values('id', 'nombre')
            data = json.dumps(list(municipios), cls=DjangoJSONEncoder)
            print(data)
        else:
            data = {}
    except:
        data = {}
        pass

    return HttpResponse(data, content_type='application/json')


def obtenerParroquias(request):
    """
    Función que permite obtener la lista de municipios asociados a un estado

    El método hace un llamado al modelo para realizar una consulta

    @param id_estado: Identificador del estado
    @type id_estado: entero

    @return: Lista de municipios asociados al estado
    """
    try:
        if Municipio.objects.exists():
            id_municipio = request.GET.get('id_municipio')
            municipios = Parroquia.objects.filter(municipio_id=id_municipio).values('id', 'nombre')
            data = json.dumps(list(municipios), cls=DjangoJSONEncoder)
        else:
            data = {}
    except:
        data = {}
        pass

    return HttpResponse(data, content_type='application/json')

def listMunicipios():
    """
    Función que permite obtener el municipio asociado a una parroquia

    El método hace un llamado a un servicio REST de la aplicación comun

    @param id_parroquia: Identificador de la parroquia
    @type id_parroquia: entero

    @return: El municipio asociado a la parroquia
    """
    try:
        if Municipio.objects.exists():
            consulta = Municipio.objects.all().values('id', 'nombre')
        else:
            consulta = [{'id': '', 'nombre': ''}]
    except:
        consulta = [{'id': '', 'nombre': ''}]

    return consulta

class LoginRequeridoPerAuth(LoginRequiredMixin, GroupRequiredMixin):
    """!
    Clase que reescribe el dispatch de LoginRequiredMixin

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """

    def dispatch(self, request, *args, **kwargs):
        """
        Envia una alerta al usuario que intenta acceder sin permisos para esta clase
        @return: Direcciona al login en caso de no poseer permisos, en caso contrario usa la clase
        """
        if not request.user.is_authenticated:
            messages.warning(self.request, "Debes iniciar Sessón")
            return self.handle_no_permission()

        valid_group = False
        grupos = request.user.groups.all()
        grupo = []
        if len(grupos) > 1:
            for g in grupos:
                grupo += str(g),
                if (str(g) in self.get_group_required()):
                    valid_group = True
        else:
            grupo = str(request.user.groups.get())
            if (grupo in self.get_group_required()):
                valid_group = True
        if not (valid_group):
            return redirect('utils:403error')
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class StartView(LoginRequeridoPerAuth, TemplateView):
    """!
    Muestra el inicio de la plataforma

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    @return: El template inicial de la plataforma
    """
    template_name = "base.inicio.html"
    group_required = [u"Administradores", u"Voceros", u"Integrantes"]


class Forbidden(TemplateView):
    """!
    Dirige a la plantilla Forbidden 403

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
    GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """
    template_name = "base.403.html"
