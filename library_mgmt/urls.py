# shophub_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),

    # Include all app URLs (e.g., login, dashboard, etc.)
    path('', include('library.urls')),

    # ✅ Logout route — redirects to 'login' page after logout
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
