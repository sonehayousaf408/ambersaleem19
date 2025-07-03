# library/urls.py  – replace everything with this
from django.urls import path
from . import views

urlpatterns = [
    # ────────────────
    # Auth
    # ────────────────
    path('login/',  views.login_view,  name='login'),   # matches LOGIN_URL in settings
    path('logout/', views.logout_view, name='logout'),

    # ────────────────
    # Dashboard Home
    # ────────────────
    path('', views.home, name='home'),

    # ────────────────
    # Feature Views
    # ────────────────
    path('employees/',        views.employee_list,    name='employee_list'),
    path('sales-report/',     views.sales_report,     name='sales_report'),   # 7‑day totals
    path('employee-sales/',   views.employee_sales,   name='employee_sales'), # per‑employee totals
    path('receipts/',         views.receipt_view,     name='receipt_view'),
    path('charts/',           views.sales_charts,     name='sales_charts'),
    path('customers/insights/', views.customer_insights, name='customer_insights'),
]
