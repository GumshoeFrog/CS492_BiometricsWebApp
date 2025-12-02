from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from .forms import BankForm
from .authenticate import BankBackend
from .models import Bank
from django.contrib.auth.hashers import check_password

# Create your views here.
def index_bank(request):
    if 'bank_id' not in request.session:
        return redirect('bank:login_bank')
    bank = Bank.objects.get(pk=request.session['bank_id'])
    context = {'bank': bank}
    return render(request, 'bank/index-bank.html', context)


def register_bank(request):
    form = BankForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('bank:index_bank')
    context = {'form': form}
    return render(request, 'bank/register-bank.html', context)


class BankLoginForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
def login_bank(request):
    form = BankLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            password = form.cleaned_data['password']

            for bank in Bank.objects.all():
                if check_password(password, bank.password):
                    request.session['bank_id'] = bank.id
                    return redirect ('bank:index_bank')
                messages.error(request, 'Password incorrect')
    context = {'form': form}
    return render(request, 'bank/login-bank.html', context)


def logout_bank(request):
    if 'bank_id' in request.session:
        del request.session['bank_id']
    messages.success(request, 'Logged out')
    return redirect('bank:index_bank')