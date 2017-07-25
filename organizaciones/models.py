# -*- coding: utf-8 -*-
"""!
    Models que construye el modelo de datos de las organizaciones sociales

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-07-2017
    @versi 1.0.0
"""

from django.db import models

from utils.models import Parroquia


class OrganizacionSocial(models.Model):
    """!
        Clase que contiene el modelo de datos de las organizaciones sociales

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 25-07-2017
        @version 1.0.0
    """
    codigo = models.CharField(max_length=16)
    rif = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(max_length=128)
    fecha_conformacion = models.DateField(auto_now=False)
    sector = models.TextField(blank=True)
    localidad = models.ForeignKey(Parroquia)
    activa = models.BooleanField(default=True)

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @version 1.0.0
        """
        ordering = ('codigo',)
        verbose_name = 'Organizacion Social'
        verbose_name_plural = 'Organizaciones Sociales'
        abstract = True

    def __str__(self):
        """!
            Fucncion que muestra la informacion de las organizaciones sociales
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos de la organizacion social
        """
        return self.codigo


class Comuna(OrganizacionSocial):
    """!
        Clase que contiene el modelo de datos de las comunas

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 25-07-2017
        @version 1.0.0
    """
    situr = models.CharField(max_length=17)

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @version 1.0.0
        """
        ordering = ('codigo',)
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'

    def __str__(self):
        """!
            Fucncion que muestra la informacion sobre las comuna
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos de la comuna
        """
        return self.codigo
