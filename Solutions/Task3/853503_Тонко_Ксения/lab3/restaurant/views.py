from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Dish, Cook, Stock, Contact, Event
from .forms import CookModelForm, ContactModelForm


def index(request):
    return render(request, 'restaurant/home.html')


def add_cook(request):
    if request.method == "POST":
        form = CookModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cooks')
    else:
        form = CookModelForm()
    return render(request, 'restaurant/cook_edit.html', {'form': form})


def edit_cook(request, pk):
    cook = get_object_or_404(Cook, pk=pk)
    form = CookModelForm(instance=cook)
    if request.method == 'POST':
        form = CookModelForm(request.POST, request.FILES, instance=cook)
        if form.is_valid():
            form.save()
            return redirect('cook-detail', pk=pk)
    return render(request, 'restaurant/cook_edit.html', {'form': form})


def delete_cook(request, pk):
    cook = Cook.objects.get(pk=pk)
    cook.delete()
    return redirect("cooks")


class DishListView(ListView):
    model = Dish
    paginate_by = 10
    ordering = ['name']


class DishDetailView(DetailView):
    model = Dish


class CookListView(ListView):
    model = Cook
    paginate_by = 10
    ordering = ['first_name', 'last_name']


class CookDetailView(DetailView):
    model = Cook


class StockListView(ListView):
    model = Stock
    paginate_by = 10
    ordering = ['start_date']


class StockDetailView(DetailView):
    model = Stock


class ContactListView(ListView):
    model = Contact
    paginate_by = 10
    ordering = ['first_name']


class ContactDetailView(DetailView):
    model = Contact


class EventListView(ListView):
    model = Event
    paginate_by = 10
    ordering = ['date']


class EventDetailView(DetailView):
    model = Event


def cont(request):
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/restaurant/show_contact')
            except:
                pass
    else:
        form = ContactModelForm()
    return render(request, 'restaurant/contact.html', {'form': form})


def show_contacts(request):
    contacts = Contact.objects.all()
    return render(request, "restaurant/show_contact.html", {'contacts': contacts})


def edit_contact(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, 'restaurant/contact_edit.html', {'contact': contact})


def update_contact(request, id):
    contact = Contact.objects.get(id=id)
    form = ContactModelForm(request.POST, instance=contact)
    if form.is_valid():
        form.save()
        return redirect("/restaurant/show_contact")
    return render(request, 'restaurant/contact_edit.html', {'contact': contact})


def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect("/restaurant/show_contact")
