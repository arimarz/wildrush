from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User
from experiences.models import Experience

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name='User')
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='reviews', verbose_name='Experience')
    rating = models.IntegerField(verbose_name='Rating', validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(verbose_name='Comment')

    def __str__(self):
        return f"{self.user.username} - {self.experience}"

    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['experience']),
        ]
