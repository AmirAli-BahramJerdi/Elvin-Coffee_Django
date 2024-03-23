from django.shortcuts import render
from products_app.models import *
from cofee_app.models import *
from contactus_app.models import Massage


def home(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(message)
        Massage.objects.create(name=name, email=email, message=message)

    left_product = Product_left.objects.all()
    right_product = Product_right.objects.all()

    left_coffee = Coffee_left.objects.all()
    right_coffee = Coffee_right.objects.all()

    return render(request, 'index.html', context={'left_product':left_product, 'right_product':right_product, 'left_coffee':left_coffee, 'right_coffee':right_coffee})