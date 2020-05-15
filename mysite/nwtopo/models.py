from django.db import models

# Create your models here.
class Template(models.Model):
    temp_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.temp_name


class Deploy(models.Model):
    title = models.CharField(max_length=100, null=True)
    temp_amount = models.IntegerField(null=True)

    def __str__(self):
        return self.title