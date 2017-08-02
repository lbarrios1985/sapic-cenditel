# -*- coding: utf-8 -*-
"""!
Formuario para generar los formulario para los usuarios

@author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
@copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
@date 29-05-2017
@version 1.0.0
"""
from captcha.fields import CaptchaField
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm, PasswordResetForm,
    SetPasswordForm, PasswordChangeForm
    )
from django.forms.fields import (
    CharField, BooleanField
)
from django.forms.widgets import (
    PasswordInput, CheckboxInput
)

from .models import UserProfile


class FormularioLogin(forms.Form):
    """!
    Clase que permite crear el formulario de ingreso a la aplicación

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """
    contrasena = CharField()
    usuario = CharField()
    remember_me = BooleanField()
    captcha = CaptchaField()

    class Meta:
        fields = ('usuario', 'contrasena', 'remember_me' 'captcha')

    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['contrasena'].widget = PasswordInput()
        self.fields['contrasena'].widget.attrs.update({'class': 'form-control',
        'placeholder': 'Contraseña'})
        self.fields['usuario'].widget.attrs.update({'class': 'form-control',
        'placeholder': 'Nombre de Usuario o Email'})
        self.fields['remember_me'].label = "Recordar"
        self.fields['remember_me'].widget = CheckboxInput()
        self.fields['remember_me'].required = False
        self.fields['captcha'].required=True


class PasswordResetForm(PasswordResetForm):
    """!
    Clase que permite sobrescribir el formulario para resetear la contraseña

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Correo'})

    def clean(self):
        cleaned_data = super(PasswordResetForm, self).clean()
        email = cleaned_data.get("email")

        if email:
            msg = "Error este email: %s, no se encuentra asociado a una cuenta\
                  " % (email)
            try:
                User.objects.get(email=email)
            except:
                self.add_error('email', msg)


class SetPasswordForm(SetPasswordForm):
    """!
    Clase que permite sobrescribir el formulario para ingresar la nueva contraseña

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """
    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Ingresa la nueva contraseña'})

        self.fields['new_password2'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Repite la nueva contraseña'})


class FormularioUpdate(ModelForm):
    """!
    Clase que permite crear el formulario para actualizar el usuario

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(FormularioUpdate, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'form-control',
        'placeholder': 'Nombres'})
        self.fields['first_name'].required=True
        self.fields['last_name'].widget.attrs.update({'class': 'form-control',
        'placeholder': 'Apellidos'})
        self.fields['last_name'].required=True
        self.fields['email'].widget.attrs.update({'class': 'form-control',
        'placeholder': 'Email'})
        self.fields['email'].required=True


class FormularioAdminUpdate(ModelForm):
    """!
    Clase que permite crear el formulario para actualizar el usuario por el administrador

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'groups',
                  'is_staff', 'is_active']

    def __init__(self, *args, **kwargs):
         super(FormularioAdminUpdate, self).__init__(*args, **kwargs)

         self.fields['first_name'].widget.attrs.update({'class': 'form-control',
         'placeholder': 'Nombres'})
         self.fields['first_name'].required=True
         self.fields['last_name'].widget.attrs.update({'class': 'form-control',
         'placeholder': 'Apellidos'})
         self.fields['last_name'].required=True
         self.fields['email'].widget.attrs.update({'class': 'form-control',
         'placeholder': 'Email'})
         self.fields['email'].required=True
         self.fields['is_staff'].label= 'Es Administrador?'
         self.fields['is_staff'].widget.attrs.update({'class': 'form-control'})
         self.fields['is_active'].label= 'Estara Activo?'
         self.fields['is_active'].widget.attrs.update({'class': 'form-control', 'checked': 'checked'})
         self.fields['groups'].widget.attrs.update({'class': 'form-control'})


class FormularioAdminRegistro(UserCreationForm):
    """!
    Clase que permite crear el formulario para crear usuario por el administrador

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email',
                  'groups', 'is_staff', 'is_active']

    def __init__(self, *args, **kwargs):
        super(FormularioAdminRegistro, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'form-control',
                                                       'placeholder':
                                                       'Nombres'})
        self.fields['first_name'].required = True
        self.fields['last_name'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder':
                                                      'Apellidos'})
        self.fields['last_name'].required = True
        self.fields['username'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder':
                                                     'Nombre de usuario \
                                                     (Username)'})
        self.fields['username'].required = True
        self.fields['password1'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder':
                                                      'Contraseña'})
        self.fields['password1'].required = True
        self.fields['password2'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder':
                                                      'Repite la Contraseña'})
        self.fields['password2'].required = True
        self.fields['email'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Email'})
        self.fields['email'].required = True
        self.fields['is_staff'].label = 'Es Administrador?'
        self.fields['is_staff'].widget.attrs.update({'class': 'form-control','data-toggle': 'toggle','data-on': 'Si',
                                                   'data-off': 'No'})
        self.fields['is_active'].label = 'Estara Activo?'
        self.fields['is_active'].widget.attrs.update({'class': 'form-control','data-toggle': 'toggle','data-on': 'Si',
                                                   'data-off': 'No',
                                                   'checked': 'checked'})
        self.fields['groups'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super(FormularioAdminRegistro, self).clean()
        email = cleaned_data.get("email")

        if email:
            msg = "Error este email: %s, ya se encuentra asociado a una cuenta\
                  " % (email)
            try:
                User.objects.get(email=email)
                self.add_error('email', msg)
            except:
                pass


class FormularioAdminRegPerfil(ModelForm):
    """!
    Clase que permite crear el formulario para actualizar usuario por el administrador

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """

    class Meta:
        model = UserProfile
        fields = ['fk_tipo_documento', 'id_perfil']

    def __init__(self, *args, **kwargs):
        super(FormularioAdminRegPerfil, self).__init__(*args, **kwargs)
        self.fields['fk_tipo_documento'].empty_label = 'Seleccione el Tipo de Documento'
        self.fields['fk_tipo_documento'].widget.attrs.update({'class': 'form-control'})
        self.fields['fk_tipo_documento'].label= 'Tipo de Documento'
        self.fields['fk_tipo_documento'].required=True
        self.fields['id_perfil'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder':'Documento de identidad'})
        self.fields['id_perfil'].label= 'Documento de Identidad'
        self.fields['id_perfil'].required=True


class PasswordChangeForm(PasswordChangeForm):
    """!
    Clase que sobrescribir el formulario para cambiar la contraseña

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Contraseña Antigua'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Ingresa la nueva contraseña'})

        self.fields['new_password2'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Repite la nueva contraseña'})
