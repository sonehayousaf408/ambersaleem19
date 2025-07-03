from django.contrib import admin
from .models import Customer, Employee, Receipt, Item, Sale

# Inline for Items under Receipts
class ItemInline(admin.TabularInline):
    model = Item
    extra = 1

# ───────────────────────────────
# Receipt Admin
# ───────────────────────────────
@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ("id", "customer", "employee", "date", "total_amount")  # ✅ FIXED
    date_hierarchy = "date"
    search_fields = ("customer__name", "employee__name")

# ───────────────────────────────
# Sale Admin
# ───────────────────────────────
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "product_name", "total", "date")  # 'total' is still valid here
    date_hierarchy = "date"
    search_fields = ("customer__name", "product_name")

# ───────────────────────────────
# Register Other Models
# ───────────────────────────────
admin.site.register(Customer)
admin.site.register(Employee)
