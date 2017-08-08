# -*- coding: utf-8 -*-
"""!
Vista que controla los procesos de las organizaciones sociales

@author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
@copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
@date 27-07-2017
@version 1.0.0
"""

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.auth.models import (
    Group, User
)
from django.core.urlresolvers import (
    reverse_lazy, reverse
)
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.views.generic.base import RedirectView
from django.views.generic.edit import (
    FormView, UpdateView
)

from .forms import (
    FormularioRegisterOrgSocial, FormsetVocero
)
from multi_form_view import MultiModelFormView

from .models import (
    OrganizacionSocial, Vocero
)

from utils.views import LoginRequeridoPerAuth

class RegisterOrgView(LoginRequeridoPerAuth, MultiModelFormView):
    """!
    Muestra el formulario de registro de la organizacion social

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 27-07-2017
    @version 1.0.0
    """
    template_name = "organizacion.register.html"
    form_classes = {
      'organizacion_social': FormularioRegisterOrgSocial,
      'voceros': FormsetVocero,
    }
    success_url = reverse_lazy('utils:inicio')
    record_id = None
    group_required = [u"Administradores"]

    def get_objects(self):
        self.record_id = self.kwargs.get('record_id', None)
        try:
            record = Vocero.objects.select_related().get(fk_org_social=self.record_id)
        except Vocero.DoesNotExist:
            record = None
        return {
          'voceros': record,
          'organizacion_social': record.fk_org_social if record else None,
        }

    def forms_valid(self, forms, **kwargs):
        """
        Valida el formulario de registro del perfil de usuario
        @return: Dirige con un mensaje de exito a el home
        """
        nueva_organizacion = forms['organizacion_social'].save()
        nuevos_voceros = self.form_classes['voceros'](self.request.POST, instance=nueva_organizacion)
        if nuevos_voceros.is_valid():
            nuevos_voceros.save()
        messages.success(self.request, "El Usuario %s registro con exito la \
                                        Organizacion Social %s"
                                         % (str(self.request.user), str(nueva_organizacion.nombre)))
        return redirect(self.success_url)

    def forms_invalid(self, forms, **kwargs):
        messages.error(self.request, "%s" % (str(forms['organizacion_social'].errors.as_data())))

        return super(RegisterOrgView, self).forms_invalid(forms)


def ListOrgView(request):
    return render(request, 'organizaciones.list.html')