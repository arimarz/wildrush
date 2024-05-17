from django.db import models
from django.conf import settings

class Provider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='provider_profile', null=True, blank=True)
    name = models.CharField(max_length=100, db_index=True, verbose_name='Name')
    location = models.CharField(max_length=255, verbose_name='Location')
    contact_info = models.CharField(max_length=100, verbose_name='Contact Info')

    def __str__(self):
        return self.name