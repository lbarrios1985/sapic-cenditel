# -*- encoding: utf-8 -*-
"""!
Vista que controla los procesos de las utilidades de la pltaforma

@author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
@copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
@date 29-05-2017
@version 1.0.0
"""

from django.contrib import messages
from django.contrib.auth.mixins import (
    PermissionRequiredMixin, LoginRequiredMixin
)
from django.shortcuts import (
    redirect, render
)
from django.views.generic import TemplateView
from braces.views import GroupRequiredMixin



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
