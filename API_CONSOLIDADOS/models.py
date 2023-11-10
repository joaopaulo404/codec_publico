from django.db import models

# Create your models here.
class Consolidados(models.Model):
    consolidado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consolidados'
