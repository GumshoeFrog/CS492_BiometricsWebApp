from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from .models import Federal

class FederalBackend:
    def authenticate(self, request, password=None, **kwargs):
        try:
            federal = Federal.objects.get(password=password)
            if check_password(password, federal.password):
                return federal
        except Federal.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Federal.objects.get(pk=user_id)
        except Federal.DoesNotExist:
            return None