from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Name')
    location = models.CharField(max_length=255, verbose_name='Location')
    contact_info = models.CharField(max_length=100, verbose_name='Contact Info')

    def __str__(self):
        return self.name