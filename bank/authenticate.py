from django.contrib.auth.hashers import check_password
from .models import Bank

class BankBackend:
    def authenticate(self, request, password=None):
        try:
            bank = Bank.objects.get(password=password)
            if check_password(password, bank.password):
                return bank
        except Bank.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Bank.objects.get(pk=user_id)
        except Bank.DoesNotExist:
            return None