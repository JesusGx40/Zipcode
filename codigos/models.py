from django.db import models
class Registros_info(models.Model):
    d_codigo= models.CharField(max_length=10)
    d_asenta= models.CharField(max_length=70)
    d_tipo_asenta= models.CharField(max_length=40)
    D_mnpio = models.CharField(max_length=40)
    d_estado = models.CharField(max_length=40)
    d_ciudad = models.CharField(max_length=40)
    d_CP= models.CharField(max_length=10)
    c_estado= models.CharField(max_length=10)
    c_oficina= models.CharField(max_length=10)
    c_CP = models.CharField(max_length=3, blank=True)
    c_tipo_asenta = models.CharField(max_length=10)
    c_mnpio= models.CharField(max_length=10)
    id_asenta_cpcons= models.CharField(max_length=6)
    d_zona= models.CharField(max_length=25)
    c_cve_ciudad= models.CharField(max_length=10)
