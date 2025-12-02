from django.shortcuts import render

# Create your views here.

def index_biometrics(request):
    # restaurant_id = request.session.get('restaurant_id')
    # if restaurant_id:
    #     restaurant = Restaurant.objects.get(pk=restaurant_id)
    #     return render(request, 'restaurant/index-restaurant.html', {'restaurant': restaurant})
    return render(request, 'biometrics/index-biometrics.html')