from django.db import models
from users.models import User
from experiences.models import Experience

class Booking(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', verbose_name='User')
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='bookings', verbose_name='Experience')
    booking_date = models.DateField(verbose_name='Booking Date')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Status')

    def __str__(self):
        return f"{self.user.username} - {self.experience}"

    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['experience']),
        ]