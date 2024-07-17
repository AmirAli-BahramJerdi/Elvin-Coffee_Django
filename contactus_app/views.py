from django.shortcuts import render, redirect

from products_app.models import (
    Product_left, Product_right
)

from cofee_app.models import (
    Coffee_left, Coffee_right
)

from .models import Massage
from .forms import SendMessageForm
from django.views import View
from django.contrib import messages



class HomeView(View):
    
    form_class = SendMessageForm
    template_name = 'index.html'
    
    def setup(self, request, *args, **kwargs):
        self.left_product = Product_left.objects.all()
        self.right_product = Product_right.objects.all()

        self.left_coffee = Coffee_left.objects.all()
        self.right_coffee = Coffee_right.objects.all()

        return super().setup(request, *args, **kwargs)

    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form, 'left_product':self.left_product, 'right_product':self.right_product, 'left_coffee':self.left_coffee, 'right_coffee':self.right_coffee})    
	    
 
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Massage.objects.create(name=cd['name'], email=cd['email'], message=cd['message'])
            messages.success(request, 'پیام شما با موفقیت ارسال شد', 'success')
            redirect("home:home")
        messages.success(request, 'ارسال پیام با مشکل همراه بود', 'danger')
        return render(request, self.template_name, context={'form':form, 'left_product':self.left_product, 'right_product':self.right_product, 'left_coffee':self.left_coffee, 'right_coffee':self.right_coffee})    
	    

