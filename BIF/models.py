from copyreg import constructor
from django.db import models

#Constantes
text_created = "Fecha de creación"
text_updated = "Fecha de actualización"

''' # Creación de los modelos.
class Inmueble(models.Model):
    numero_predial = models.CharField(max_length=30, primary_key=True)
    numero_predial_nacional = models.CharField(max_length=50, null=True, blank=True)
    sector = models.CharField(max_length=100, null=True, blank=True)
    nombre = models.TextField(null=True, blank=True)
    establecimiento = models.CharField(max_length=200, null=True, blank=True)
    tipo_documento= models.CharField(max_length=100, null=True, blank=True)
    numero_documento= models.CharField(max_length=100, null=True, blank=True)
    notaria = models.CharField(max_length=100, null=True, blank=True)
    fecha_documento = models.DateField(null=True, blank=True)
    numero_escritura = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    localizacion = models.CharField(max_length=100, null=True, blank=True)
    uso= models.CharField(max_length=100, null=True, blank=True)
    matricula = models.CharField(max_length=100, null=True, blank=True)
    propietario = models.CharField(max_length=100, null=True, blank=True)
    area= models.FloatField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    coordenadas = models.TextField(null=True, blank=True)
    ciudadela_educativa= models.CharField(max_length=50,null=True, blank=True)
    archivo = models.FileField(upload_to='staticfiles/files', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Inmueble"
        verbose_name_plural = "Inmuebles" '''


class Property(models.Model):
    predial = models.CharField(max_length=60, null=True, blank=True)
    alternative_predial = models.CharField(max_length=60, null=True, blank=True)
    appraisal = models.CharField(max_length=60, null=True, blank=True)
    document_type = models.CharField(max_length=100, null=True, blank=True)
    act = models.CharField(max_length=100, null=True, blank=True)
    document_number = models.CharField(max_length=50, null=True, blank=True)
    real_state_register = models.CharField(max_length=100, null=True, blank=True)
    document_date = models.DateField(null=True, blank=True)
    coordenates = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='staticfiles/files', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    def __str__(self):
        return self.predial

    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"
    
    
class Status(models.Model):
    id_property = models.OneToOneField("Property", related_name="status", on_delete=models.CASCADE)
    number = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    type_property = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    video = models.TextField(null=True, blank=True)
    addres = models.TextField(null=True, blank=True)
    class_property = models.CharField(max_length=50, null=True, blank=True)
    use = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Situación del inmueble"
        verbose_name_plural = "Situación de los inmuebles"    


class Licence(models.Model):
    id_property = models.OneToOneField("Property", related_name="licence", on_delete=models.CASCADE)
    curation = models.CharField(max_length=100, null=True, blank=True)
    modality = models.CharField(max_length=100, null=True, blank=True)
    type_construction = models.CharField(max_length=100, null=True, blank=True)
    licence_number = models.CharField(max_length=100, null=True, blank=True)
    licence_date = models.DateField(null=True, blank=True)
    construction_date = models.DateField(null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.licence_number

    class Meta:
        verbose_name = "Licencia"
        verbose_name_plural = "Licencias"

class Occupancy(models.Model):
    id_property = models.OneToOneField("Property", related_name="occupancy", on_delete=models.CASCADE)
    owner = models.CharField(max_length=100, null=True, blank=True)
    contract = models.CharField(max_length=100, null=True, blank=True)
    type_occupancy = models.CharField(max_length=100, null=True, blank=True)
    id_document = models.CharField(max_length=100, null=True, blank=True)
    ocuppancy_document = models.CharField(max_length=100, null=True, blank=True)
    ocuppancy_name = models.CharField(max_length=100, null=True, blank=True)
    seppi = models.CharField(max_length=100, null=True, blank=True)
    observation = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.owner

    class Meta:
        verbose_name = "Ocupación"
        verbose_name_plural = "Ocupaciones"