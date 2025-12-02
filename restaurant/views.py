from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from .forms import RestaurantForm
from .authenticate import RestaurantBackend
from .models import Restaurant
from django.contrib.auth.hashers import check_password



# Create your views here.
def index_restaurant(request):
    #if a session id is not made, redirect the user to the login page
    if 'restaurant_id' not in request.session:
        return redirect('restaurant:login_restaurant')
    #if the user is logged in, place the session ID information into the restaurant variable
    restaurant = Restaurant.objects.get(pk=request.session['restaurant_id'])
    context = {'restaurant': restaurant}
    return render(request, 'restaurant/index-restaurant.html', context)

    # restaurant_id = request.session.get('restaurant_id')
    # if restaurant_id:
    #     restaurant = Restaurant.objects.get(pk=restaurant_id)
    #     return render(request, 'restaurant/index-restaurant.html', {'restaurant': restaurant})
    # return render(request, 'restaurant/index-restaurant.html')


def register_restaurant(request):
    # Creates a post form using the Restaurant form from forms.py
    form = RestaurantForm(request.POST or None)
    # if the form is using post and the form is valid...

    if request.method == 'POST':
        # form = RestaurantForm(request.POST)
        if form.is_valid():
            # save the form and bring the user to the home page
            form.save()
            return redirect('restaurant:index_restaurant')
    context = {'form': form}
    return render(request, 'restaurant/register-restaurant.html', context)

# form class used to display email and password requests
class RestaurantLoginForm(forms.Form):
    # email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
def login_restaurant(request):
    # Creates a post form using the above login form class
    form = RestaurantLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # If the form is valid, take in the given password
            # email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            for restaurant in Restaurant.objects.all():
                if check_password(password, restaurant.password):
                    request.session['restaurant_id'] = restaurant.id
                    return redirect ('restaurant:index_restaurant')
                messages.error(request, 'Password incorrect')
    context = {'form': form}
    return render(request, 'restaurant/login-restaurant.html', context)

            # Authenticate the taken information using the backend from authenticate.py
            # backend = RestaurantBackend()
            # restaurant = backend.authenticate(request, password=password)
            # if restaurant:
            #     # if the information exists in the database,
            #     # create a session key and load the home page
            #     request.session['restaurant_id'] = restaurant.id
            #     return redirect('restaurant:index_restaurant')
            # else:
            #     # Create an error message, staying on the login page.
            #     messages.error(request, 'Email or password incorrect')
    # return render(request, 'restaurant/login-restaurant.html', {'form': form})


def logout_restaurant(request):
    # If a session ID is made, delete the user information from it, logging them out
    if 'restaurant_id' in request.session:
        del request.session['restaurant_id']
    messages.success(request, 'Logged out')
    return redirect('restaurant:index_restaurant')