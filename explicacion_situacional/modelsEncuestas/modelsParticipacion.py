# -*- coding: utf-8 -*-
"""
SAPIC

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida - https://planificacion.cenditel.gob.ve/trac/wiki/WikiStart#a5.-SistemaAutomatizadodePlanificaciónIntegralComunalSAPIC
"""
## @package explicacion_situacional.modelsEncuestas.modelsParticipacion
#
# Modelos correspondientes a la aplicación consulta
# @author Rodrigo Boet (rboet at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0
from __future__ import unicode_literals
from django.contrib.auth.models import User
from explicacion_situacional.modelsEncuestas.modelsConsultas import Opcion, Pregunta

from django.db import models


class RespuestaSino(models.Model):
    """!
    Clase que gestiona las respuestas con si/no

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 27-03-2017
    @version 1.0.0
    """
    ## Relación con la pregunta
    pregunta = models.ForeignKey(Pregunta)

    ## Respuesta
    respuesta = models.BooleanField()

    ## Id del ente adscrito
    ente_adscrito = models.IntegerField()

    ## Relación con el user
    user = models.ForeignKey(User)

class RespuestaOpciones(models.Model):
    """!
    Clase que gestiona las respuestas con opciones

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 27-03-2017
    @version 1.0.0
    """
    ## Relación con la opción de la respuesta
    opcion = models.ForeignKey(Opcion)

    ## Id del ente adscrito
    ente_adscrito = models.IntegerField()

    ## Relación con el user
    user = models.ForeignKey(User)


class RespuestaAbierta(models.Model):
    """!
    Clase que gestiona las respuestas abiertas y con justifiación

    @author Rodrigo Boet (rboet at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 27-03-2017
    @version 1.0.0
    """
    ## Texto de la respuesta
    texto_respuesta = models.TextField()

    ## Relación con la pregunta
    pregunta = models.ForeignKey(Pregunta)

    ## Id del ente adscrito
    ente_adscrito = models.IntegerField()

    ## Si la pregunta es de justificación
    es_justificacion = models.BooleanField(default=False)

    ## Relación con el user
    user = models.ForeignKey(User)