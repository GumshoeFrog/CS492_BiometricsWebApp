from django.contrib.auth.hashers import check_password
from .models import Restaurant

class RestaurantBackend:
    # authenticate function takes in the user inputs
    def authenticate(self, request, email=None, password=None):
        try:
            # create a user ticket based on the email registered in the database
            restaurant = Restaurant.objects.get(password=password)
            # if the django password check finds the password input to
            # match the password found in the database, return the user info
            if check_password(password, restaurant.password):
                return restaurant
        #if the object does not exist in the Restaurant database, return nothing
        except Restaurant.DoesNotExist:
            return None

    # gets Restaurant object based on ID primary key
    def get_user(self, user_id):
        try:
            # if ID exists, the user information is returned
            return Restaurant.objects.get(pk=user_id)
        # If the object doesn't exist, nothing is returned
        except Restaurant.DoesNotExist:
            return None

    # def authenticate_restaurant(email, password):
    #     try:
    #         restaurant = Restaurant.objects.get(email=email)
    #         if check_password(password, restaurant.password):
    #             return restaurant
    #     except Restaurant.DoesNotExist:
    #         return None