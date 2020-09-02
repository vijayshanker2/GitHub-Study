from django.shortcuts import render
from .models import Flight,Airport,Passenger
from django.http import HttpResponseRedirect

from django.urls import reverse

# Create your views here.

def index(request):
    list = Flight.objects.all()
    return render(request, "flights/index.html", {"flights": list})

def flight(request,flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        return render(request,"flights/flight.html")

    return render(request,"flights/flight.html",{
    "flight":flight,
    "passengers":flight.passengers.all(),
    "non_passengers":Passenger.objects.exclude(flight=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))
        passenger.flight.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
