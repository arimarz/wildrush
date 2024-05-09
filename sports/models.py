from django.db import models

# Define choices for adventure categories
ADVENTURE_CHOICES = (
    ('Outdoor', 'Outdoor Adventure'),
    ('Water', 'Water Adventure'),
    ('Air', 'Air Adventure'),
    ('Extreme', 'Extreme Adventure'),
    # sample for now, I'll add more in later
)

class Sport(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    category = models.CharField(max_length=100, verbose_name='Category', choices=ADVENTURE_CHOICES)

    def __str__(self):
        return self.name