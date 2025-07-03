from django.shortcuts import render

# Create your views here.
# analytics/views.py

from django.shortcuts import render
from django.db.models import Sum
from library.models import Customer  # use your actual model

def top_customers(request):
    customers = (
        Customer.objects
        .annotate(total_spent=Sum('total_spent'))
        .order_by('-total_spent')[:5]
    )
    return render(request, "analytics/top_customers.html", {"records": customers})
