from django.db import models

class apis(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    auth = models.CharField(max_length=50)
    https = models.BooleanField()
    cors = models.BooleanField()
    link = models.CharField(max_length=70)
    category = models.CharField(max_length=30)

    verbose_name = 'Api'
    verbose_name_plural = 'Apis'

    def __str__(self):
        return self.name