from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from .forms import FederalForm
from .authenticate import FederalBackend
from .models import Federal
from django.contrib.auth.hashers import check_password

# Create your views here.
def index_federal(request):
    if 'federal_id' not in request.session:
        return redirect('federal:login_federal')
    federal = Federal.objects.get(pk=request.session['federal_id'])
    context = {'federal': federal}
    return render(request, 'federal/index-federal.html', context)


def register_federal(request):
    form = FederalForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('federal:index_federal')
    context = {'form': form}
    return render(request, 'federal/register-federal.html', context)


class FederalLoginForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
def login_federal(request):
    form = FederalLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            password = form.cleaned_data['password']

            for federal in Federal.objects.all():
                if check_password(password, federal.password):
                    request.session['federal_id'] = federal.id
                    return redirect ('federal:index_federal')
                messages.error(request, 'Password incorrect')
    context = {'form': form}
    return render(request, 'federal/login-federal.html', context)


def logout_federal(request):
    if 'federal_id' in request.session:
        del request.session['federal_id']
    messages.success(request, 'Logged out')
    return redirect('federal:index_federal')