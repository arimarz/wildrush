from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review
from django.core.mail import send_mail

@receiver(post_save, sender=Review)
def send_review_notification(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'New Review Posted',
            'A new review has been posted for your listing.',
            'from@example.com',
            [instance.provider.email],
            fail_silently=False,
        )