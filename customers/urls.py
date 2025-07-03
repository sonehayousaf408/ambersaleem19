# customers/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # When someone visits /customers/, this view will be used
    path('', views.top_customers, name='customer_insights'),
]
