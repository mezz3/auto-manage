from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.
class VM_pg(models.Model):
    vm_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.vm_name