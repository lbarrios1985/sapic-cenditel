# -*- coding: utf-8 -*-
"""!
    Models que construye el modelo de datos de las organizaciones sociales

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 25-07-2017
    @versi 1.0.0
"""

from django.db import models

from utils.models import (
    Parroquia, TipoOrganizacion, TipoDocumento
)



class OrganizacionSocial(models.Model):
    """!
        Clase que contiene el modelo de datos de las organizaciones sociales

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 25-07-2017
        @version 1.0.0
    """
    fk_tipo_organizacion = models.ForeignKey(TipoOrganizacion)
    codigo = models.CharField(max_length=16)
    rif = models.CharField(max_length=12, unique=True)
    situr = models.CharField(max_length=17)
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


class MovimientoSocial(models.Model):
    """!
        Clase que contiene el modelo de datos de los Movimientos Sociales

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 25-07-2017
        @version 1.0.0
    """
    nombre = models.CharField(max_length=256, unique=True)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @version 1.0.0
        """
        ordering = ('nombre',)
        verbose_name = 'Movimiento Social'
        verbose_name_plural = 'Movimientos Sociales'

    def __str__(self):
        """!
            Fucncion que muestra la informacion sobre los Movimientos Sociales
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos de el Movimiento Social
        """
        return self.nombre


class ComunaConsejoComunal(models.Model):
    """!
        Clase que contiene el modelo de datos de los Consejos Comunales Relacionados a las Comunas

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 25-07-2017
        @version 1.0.0
    """
    fk_comuna = models.ForeignKey(OrganizacionSocial, related_name='comuna')
    fk_consejo_comunal = models.OneToOneField(OrganizacionSocial, related_name='consejo_comunal')

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @version 1.0.0
        """
        ordering = ('fk_comuna',)
        verbose_name = 'Consejo Comunal asociado a Comuna'
        verbose_name_plural = 'Consejos Comunales asociados a las Comunas'
        unique_together = (("fk_comuna", "fk_consejo_comunal"),)

    def __str__(self):
        """!
            Fucncion que muestra la informacion sobre los Consejos Comunales asociados a las Comunas
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos de el Consejo Comunal asociado a Comuna
        """
        return self.pk


class ComunaOrgSociproductiva(models.Model):
    """!
        Clase que contiene el modelo de datos de las organizaciones Socioproductivas Relacionadas a las comunas

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 25-07-2017
        @version 1.0.0
    """
    fk_comuna = models.ForeignKey(OrganizacionSocial, related_name='comunas')
    fk_ospc = models.OneToOneField(OrganizacionSocial, related_name='opsc')

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @version 1.0.0
        """
        ordering = ('fk_comuna',)
        verbose_name = 'Organizacion Socioproductiva relacionada a la comuna'
        verbose_name_plural = 'Organizaciones Socioproductivas relacionadas a las comunas'
        unique_together = (("fk_comuna", "fk_ospc"),)

    def __str__(self):
        """!
            Fucncion que muestra la informacion sobre las Organizaciones Socioproductivas Relacionadas a las Comunas
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos de la  Organizacion Socioproductiva relacionada a la comuna
        """
        return self.pk


class ComunaMovimientoSocial(models.Model):
    """!
        Clase que contiene el modelo de datos de los Movimientos Sociales Relacionados a las Comunas

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 25-07-2017
        @version 1.0.0
    """
    fk_comuna = models.ForeignKey(OrganizacionSocial,  related_name='comunas_mov')
    fk_mov_social = models.ForeignKey(MovimientoSocial)

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @version 1.0.0
        """
        ordering = ('fk_comuna',)
        verbose_name = 'Movimiento Social Relacionado a la Comuna'
        verbose_name_plural = 'Movimientos Sociales Relacionados a las Comunas'
        unique_together = (("fk_comuna", "fk_mov_social"),)

    def __str__(self):
        """!
            Fucncion que muestra la informacion sobre los Movimientos Sociales Relacionados a las Comunas
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos del Movimiento Social Relacionado a la Comuna
        """
        return self.pk


class Vocero(models.Model):
    """!
        Clase que contiene el modelo de datos de los Voceros

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 25-07-2017
        @version 1.0.0
    """
    fk_tipo_documento = models.ForeignKey(TipoDocumento)
    nombres = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=120)
    documento_identidad = models.PositiveIntegerField(unique=True)
    sector = models.TextField(blank=True, null=True)
    casa_edificio_calle = models.TextField(blank=True, null=True)
    localidad = models.ForeignKey(Parroquia, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @version 1.0.0
        """
        ordering = ('documento_identidad',)
        verbose_name = 'Vocero'
        verbose_name_plural = 'Voceros'

    def __str__(self):
        """!
            Fucncion que muestra la informacion sobre los Voceros
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos del Vocero
        """
        return self.documento_identidad


class VoceroOrganizacionSocial(models.Model):
    """!
        Clase que contiene el modelo de datos de los Voceros asociados a las organizacione sociales

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 25-07-2017
        @version 1.0.0
    """
    fk_org_social = models.ForeignKey(OrganizacionSocial)
    fk_vocero = models.ForeignKey(Vocero)

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @version 1.0.0
        """
        ordering = ('fk_vocero',)
        verbose_name = 'Vocero asociado a la Organizacion Social'
        verbose_name_plural = 'Voceros asociados a las Organizaciones Sociales'
        unique_together = (("fk_org_social", "fk_vocero"),)

    def __str__(self):
        """!
            Fucncion que muestra la informacion sobre los Voceros asociados a las organizacione sociales
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 25-07-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos del Vocero asociado a la Organizacion Social
        """
        return self.fk_vocero
