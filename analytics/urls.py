# library_lms_django/analytics/urls.py

from django.urls import path
from . import views

app_name = "analytics"          # 🔗 gives your URLs a namespace

urlpatterns = [
    # /analytics/top-customers/
    path("top-customers/", views.top_customers, name="top_customers"),
]
