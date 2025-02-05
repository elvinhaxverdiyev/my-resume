from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Home, About, Portfolio, Role
from .forms import ContactForm

def home_view(request):
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

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was sent successfully!")
            return redirect("home")
        else:
            messages.error(request, "Error! Something went wrong.")
    else:
        form = ContactForm()

    return render(request, "home.html", {"form": form})
