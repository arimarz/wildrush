from django.db import models
from users.models import User 
from experiences.models import Experience

class CalendarEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calendar_events', verbose_name='User')
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='calendar_events', verbose_name='Experience')
    event_date = models.DateField(verbose_name='Event Date')

    def __str__(self):
        return f"{self.user.username} - {self.experience}"

    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['experience']),
        ]
