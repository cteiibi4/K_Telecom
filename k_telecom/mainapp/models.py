from django.db import models


# Create your models here.

class TypeEquipment(models.Model):
    code = models.IntegerField
    name_type = models.CharField(max_length=50)
    mask_serial_number = models.CharField(max_length=10)


class Equipment(models.Model):
    code = models.IntegerField
    code_type = models.ForeignKey(TypeEquipment, on_delete=models.CASCADE)
    serial_number = models.CharField(unique=True, max_length=10)

