# -*- coding: utf-8 -*-
from django.contrib.gis import forms
#from django.forms import ModelForm

from explicacion_situacional.modelsExplicacion.modelsExplicacionesSituacional import *


class ExplicacionForms(forms.ModelForm):

    class Meta:
        model = ExplicacionSituacional
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExplicacionForms, self).__init__(*args, **kwargs)
        self.fields['fk_organizacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['fk_organizacion'].empty_label = 'Seleccione la organizacion social'
        self.fields['fk_organizacion'].label = 'Organizacion Social'
        self.fields['fk_organizacion'].required=True

        self.fields['coordenadas'].widget=forms.OSMWidget(attrs = {'map_width': 600, 'map_height': 400, 'default_lat':8, 'default_lon':-66})
        self.fields['coordenadas'].required=True 