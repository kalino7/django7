from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    books = "Mr Booker T"
    return render(request, 'bookings/index.html', {
        "bookings":books
    })
