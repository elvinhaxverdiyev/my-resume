from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.views import View

from .models import Home, About, Portfolio, Role
from .forms import ContactForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        home_items = Home.objects.all()
        about_item = About.objects.first()
        portfolio_items = Portfolio.objects.all()
        role_list = Role.objects.all()
        
        form = ContactForm()

        return render(request, "home.html", {
            "home_items": home_items,
            "about_item": about_item,
            "portfolio_items": portfolio_items,
            "role_list": role_list,
            "form": form
        })



class ContactView(View):
    
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, "home.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was sent successfully!")
            return redirect("home") 
        else:
            messages.error(request, "Error! Something went wrong.")
            return render(request, "home.html", {"form": form}) 