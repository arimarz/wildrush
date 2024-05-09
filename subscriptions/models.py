from django.db import models
from users.models import User
from providers.models import Provider

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions', verbose_name='User')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='subscriptions', verbose_name='Provider')
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')

    def __str__(self):
        return f"{self.user.username} - {self.provider.name}"

    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['provider']),
        ]