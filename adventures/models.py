from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.utils.translation import gettext_lazy as _

# User model represents a user in the system
class User(models.Model):
    # Username field with regex validation
    username = models.CharField(max_length=150, unique=True, validators=[RegexValidator(
        regex='^[a-zA-Z0-9._]+$',
        message=_('Enter a valid username. This value may contain only letters, numbers, dots, and underscores.'),
        code='invalid_username'
    )], db_index=True)  # Add index to 'username' field)
    # Email field with email format validation
    email = models.EmailField(unique=True, validators=[EmailValidator(message=_('Enter a valid email address.'))], db_index=True)  # Add index to 'email' field
    password = models.CharField(max_length=128)  # Password field
    first_name = models.CharField(max_length=55)  # First name field
    last_name = models.CharField(max_length=55)  # Last name field

    def __str__(self):
        return self.username

# Sport model represents different adventure sports
class Sport(models.Model):
    name = models.CharField(max_length=100, db_index=True)  # Add index to 'name' field
    description = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Provider model represents companies or individuals providing adventure experiences
class Provider(models.Model):
    name = models.CharField(max_length=100, db_index=True)  # Add index to 'name' field
    location = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Experience model represents individual adventure experiences offered by providers
class Experience(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE) # Foreign key to Sport model
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE) # Foreign key to Provider model
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.sport.name} - {self.provider.name}"
    
    class Meta:
        indexes = [
            models.Index(fields=['sport']),  # Add index to 'sport' field
            models.Index(fields=['provider']),  # Add index to 'provider' field
        ]

# Booking model represents bookings made by users for specific adventure experiences
class Booking(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to User model
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)  # Foreign key to Experience model
    booking_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.experience}"
    
    class Meta:
        indexes = [
            models.Index(fields=['user']),  # Add index to 'user' field
            models.Index(fields=['experience']),  # Add index to 'experience' field
        ]

# Review model represents reviews submitted by users for specific adventure experiences
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign key to User model
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE) # Foreign key to Experience model
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.experience}"
    
    class Meta:
        indexes = [
            models.Index(fields=['user']),  # Add index to 'user' field
            models.Index(fields=['experience']),  # Add index to 'experience' field
        ]

# CalendarEvent model represents events scheduled by users for specific adventure experiences
class CalendarEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign key to User model
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE) # Foreign key to Experience model
    event_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.experience}"
    
    class Meta:
        indexes = [
            models.Index(fields=['user']),  # Add index to 'user' field
            models.Index(fields=['experience']),  # Add index to 'experience' field
        ]

# Subscription model represents subscriptions made by users to specific adventure providers
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign key to User model
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE) # Foreign key to Provider model
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.provider.name}"
    
    class Meta:
        indexes = [
            models.Index(fields=['user']),  # Add index to 'user' field
            models.Index(fields=['provider']),  # Add index to 'provider' field
        ]
