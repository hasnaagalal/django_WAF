from django.db import models

class ip(models.Model):
    ip_address = models.GenericIPAddressField()
