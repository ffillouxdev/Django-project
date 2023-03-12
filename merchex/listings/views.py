from listings.models import Band
from listings.models import Contact
from listings.models import Listing
from listings.models import Abt
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})
    
def about(request):
    abts = Abt.objects.all()
    return render(request, 'listings/about.html', {'abts': abts})

def listings(request):
   listings = Listing.objects.all()
   return render(request, 'listings/listings.html', {'listings':listings})

def contact_us(request):
    contacts = Contact.objects.all()
    print(request.headers)
    if 'User' in request.headers:
        if request.headers["User"] == 'florian':
            return render(request, 'listings/contact.html', {'contact': contacts})
    return render(request, 'listings/error.html')
    

