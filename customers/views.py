# customers/views.py

from django.shortcuts import render
from .models import Customer  # Make sure the Customer model exists in customers/models.py

def top_customers(request):
    customers = Customer.objects.all()  # You can filter or sort later
    return render(request, 'customers/insights.html', {'customers': customers})
