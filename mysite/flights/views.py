from django.shortcuts import render
from .models import Flight
from django.http import  Http404


# Create your views here.

def index(request):
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, "flights/index.html", context)


def flights(request, flight_id):
    try:
        flights_id = Flight.objects.get(pk=flight_id)

    except Flight.DoesNotExist:
        raise Http404("Flight do Title's not exist")

    context = {
        "flights": flights_id
    }

    return render(request, "flights/flights.html", context)
