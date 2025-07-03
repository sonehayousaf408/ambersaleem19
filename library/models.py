from django.db import models

# ───────────────────────────────
# Book
# ───────────────────────────────
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

# ───────────────────────────────
# Customer
# ───────────────────────────────
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    total_spent = models.FloatField()
    loyalty_points = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

# ───────────────────────────────
# Employee
# ───────────────────────────────
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# ───────────────────────────────
# Sale
# ───────────────────────────────
class Sale(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="sales",
    )
    product_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    total = models.IntegerField()

    def __str__(self):
        customer_name = getattr(self.customer, "name", "Unknown Customer")
        return f"Sale #{self.id} • {self.product_name} • {customer_name} • Rs.{self.total}"

# ───────────────────────────────
# Receipt (UPDATED for employee and total_amount)
# ───────────────────────────────
class Receipt(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # ✅ Added employee FK
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # ✅ Renamed from `total`
    date = models.DateField()

    def __str__(self):
        customer_name = getattr(self.customer, "name", "Unknown Customer")
        employee_name = getattr(self.employee, "name", "Unknown Employee")
        return f"Receipt #{self.id} • {customer_name} • By {employee_name}"

# ───────────────────────────────
# Item
# ───────────────────────────────
class Item(models.Model):
    receipt = models.ForeignKey(
        Receipt,
        related_name="items",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        receipt_id = getattr(self.receipt, "id", "?")
        return f"{self.name} x{self.quantity} (Receipt {receipt_id})"
