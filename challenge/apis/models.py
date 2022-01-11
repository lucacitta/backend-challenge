from django.db import models

class Apis(models.Model):
    API = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    Auth = models.CharField(max_length=50, null=True, blank=True)
    HTTPS = models.BooleanField()
    Cors = models.BooleanField(null=True)
    Link = models.CharField(max_length=150)
    Category = models.CharField(max_length=30)

    verbose_name = 'Api'
    verbose_name_plural = 'Apis'

    def __str__(self):
        return self.name