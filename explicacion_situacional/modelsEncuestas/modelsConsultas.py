# -*- coding: utf-8 -*-
"""
Sistema de Consulta Pública

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida - https://planificacion.cenditel.gob.ve/trac/wiki/WikiStart#a5.-SistemaAutomatizadodePlanificaciónIntegralComunalSAPIC
"""
## @package explicacion_situacional.modelsEncuestas.modelsConsultas
#
# Modelos correspondientes a la aplicación consulta
# @author Rodrigo Boet (rboet at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Consulta(models.Model):
    """!
    Clase que gestiona los datos de la consulta

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 15-02-2017
    @version 1.0.0
    """
    ## Nombre de la consulta
    nombre_consulta = models.CharField(max_length=50, unique=True)

    ## Estado de la consulta
    activa = models.BooleanField(default=True)

    ## Relación con el user
    user = models.ForeignKey(User)


class TipoPregunta(models.Model):
    """!
    Clase que gestiona los tipos de preguntas

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 15-02-2017
    @version 1.0.0
    """
    ## Nombre de la consulta
    tipo = models.CharField(max_length=30)

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 13-07-2017
            @version 1.0.0
        """
        ordering = ('tipo',)
        verbose_name = 'Tipo Pregunta'
        verbose_name_plural = 'Tipos de Preguntas'

    def __str__(self):
        """!
            Funcion que muestra la informacion de los tipos de preguntas
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 13-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos del tipo de pregunta
        """
        return self.tipo


class Pregunta(models.Model):
    """!
    Clase que gestiona los datos de la pregunta

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 15-02-2017
    @version 1.0.0
    """
    ## Texto de la pregunta
    texto_pregunta = models.TextField()

    ## Relación con el tipo de pregunta
    tipo_pregunta = models.ForeignKey(TipoPregunta)

    ## Relación con la consulta
    consulta = models.ForeignKey(Consulta)


class Opcion(models.Model):
    """!
    Clase que gestiona las opciones de las preguntas

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 15-02-2017
    @version 1.0.0
    """
    ## Texto de la opción
    texto_opcion = models.TextField()

    ## Relación con la pregunta
    pregunta = models.ForeignKey(Pregunta)
