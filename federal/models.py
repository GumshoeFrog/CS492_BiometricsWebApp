from django.db import models
from django.contrib.auth.models import make_password
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Federal(models.Model):
    organization = models.CharField(max_length=100, default="Department of Human Intelligence")
    password = models.CharField(max_length=600)
    email = models.EmailField(max_length=100, unique=True, default="example@example.com")

@receiver(pre_save, sender=Federal)
def hash_password(sender, instance, **kwargs):
    if not instance.password.startswith('pbkdf2_'):
        instance.password = make_password(instance.password)