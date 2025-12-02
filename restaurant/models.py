from django.db import models
from django.contrib.auth.models import make_password
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
# Create a database table named Restaurant
class Restaurant(models.Model):
    # Column 1: Organization ID given to the entity requesting our 3rd party services
    organization = models.CharField(max_length=100, default="Restaurant Co.")
    # Column 2: biometric signature taken from the scanner
    password = models.CharField(max_length=600)
    # Column 3: User's email for data recovery and new password requests
    email = models.EmailField(max_length=100, unique=True, default="example@example.com")

# obtain the password data from the Restaurant database and modify it before it's saved
@receiver(pre_save, sender=Restaurant)
# hash password function takes the origin database, the object to be called from the database, and extra information
def hash_password(sender, instance, **kwargs):
    # if the password field item does not start with 'pbkdf2_'...
    if not instance.password.startswith('pbkdf2_'):
        # use django's make_password to hash the item in the given password field using PBKDF2 (a slow hash function).
        instance.password = make_password(instance.password)

