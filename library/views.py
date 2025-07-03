# library/views.py  – replace everything with this
from datetime import date, timedelta, datetime
from decimal import Decimal

from django.db.models import Sum, Value, FloatField
from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect
from django.utils import timezone

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Customer, Employee, Receipt, Item
from sales.models import Sale

# ────────────────────────────────
# Auth Views
# ────────────────────────────────
def login_view(request):
    """
    Custom login that falls back to Django‑auth.
    Redirects authenticated users straight to the dashboard.
    """
    if request.user.is_authenticated:
        return redirect('home')            # already logged in

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')        # dashboard
        else:
            return render(
                request,
                'library/login.html',
                {'error': 'Invalid credentials'}
            )

    return render(request, 'library/login.html')


def logout_view(request):
    """
    Ends the session and sends the user back to the login screen.
    """
    logout(request)
    return redirect('login')


# ────────────────────────────────
# Dashboard / Home
# ────────────────────────────────
@login_required
def home(request):
    return render(request, 'library/home.html')


# ────────────────────────────────
# Customer Insights
# ────────────────────────────────
@login_required
def customer_insights(request):
    customers = (
        Customer.objects
        .annotate(total=Coalesce('total_spent', Value(0.0), output_field=FloatField()))
        .order_by('-total')
    )
    return render(request, 'library/customer_insights.html', {'customers': customers})


# ────────────────────────────────
# Employees List
# ────────────────────────────────
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'library/employee_list.html', {'employees': employees})


# ────────────────────────────────
# Sales Report (last 7 days)
# ────────────────────────────────
@login_required
def sales_report(request):
    today = timezone.now().date()
    last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]

    sales_data = []
    for day in last_7_days:
        start = datetime.combine(day, datetime.min.time())
        end = datetime.combine(day, datetime.max.time())
        total = (
            Sale.objects
            .filter(date__range=(start, end))
            .aggregate(total=Sum('total'))
            .get('total')
        ) or Decimal('0')

        sales_data.append({
            'date': day.strftime('%Y-%m-%d'),
            'total': float(total),
        })

    return render(request, 'library/sales_report.html', {'sales_data': sales_data})


# ────────────────────────────────
# Receipts with Items
# ────────────────────────────────
@login_required
def receipt_view(request):
    receipts = Receipt.objects.prefetch_related('items').all()
    return render(request, 'library/receipt_view.html', {'receipts': receipts})


# ────────────────────────────────
# Sales Charts (daily + top items)
# ────────────────────────────────
@login_required
def sales_charts(request):
    today = date.today()
    week_ago = today - timedelta(days=6)

    # Daily totals (dict keyed by date)
    raw_data = (
        Receipt.objects
        .filter(date__range=(week_ago, today))
        .values('date')
        .annotate(total=Sum('total_amount'))
        .order_by('date')
    )
    date_totals = {entry['date']: float(entry['total']) for entry in raw_data}

    daily_sales = []
    for i in range(7):
        day = week_ago + timedelta(days=i)
        daily_sales.append({
            'date': day.strftime('%Y-%m-%d'),
            'total': date_totals.get(day, 0.0),
        })

    # Top‑5 items by quantity
    item_sales = (
        Item.objects
        .filter(receipt__date__range=(week_ago, today))
        .values('name')
        .annotate(quantity=Sum('quantity'))
        .order_by('-quantity')[:5]
    )

    return render(request, 'library/sales_charts.html', {
        'daily_sales': daily_sales,
        'item_sales': item_sales,
    })


# ────────────────────────────────
# Employee Sales (totals)
# ────────────────────────────────
@login_required
def employee_sales(request):
    sales_data = (
        Receipt.objects
        .values('employee__id', 'employee__name')
        .annotate(total_sales=Sum('total_amount'))   # correct field name
        .order_by('-total_sales')
    )
    return render(request, 'library/employee_sales.html', {'sales_data': sales_data})
