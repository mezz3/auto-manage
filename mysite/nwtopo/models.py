from django.db import models

# Create your models here.
class Template(models.Model):
    title = models.CharField(max_length=100, null=True)
    # temp_file = models.FileField(upload_to='template/file/', null=True)
    temp_amount = models.IntegerField(null=True)

    def __str__(self):
        return self.title