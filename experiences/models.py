from django.db import models
from sports.models import Sport
from providers.models import Provider

class Experience(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='experiences', verbose_name='Sport')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='experiences', verbose_name='Provider')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    duration = models.CharField(max_length=50, verbose_name='Duration')
    capacity = models.IntegerField(verbose_name='Capacity')

    def __str__(self):
        return f"{self.sport.name} - {self.provider.name}"

    class Meta:
        indexes = [
            models.Index(fields=['sport']),
            models.Index(fields=['provider']),
        ]