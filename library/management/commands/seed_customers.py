from django.core.management.base import BaseCommand
from faker import Faker
from library.models import Customer  # Make sure this is the correct path

fake = Faker()

class Command(BaseCommand):
    help = "Seed the Customer table with fake data"

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=50,
                            help="Number of customers to create (default 50)")

    def handle(self, *args, **options):
        count = options["count"]
        customers = []

        for _ in range(count):
            customers.append(
                Customer(
                    name=fake.name(),
                    total_spent=fake.random_int(min=0, max=50000),
                    loyalty_points=fake.random_int(min=0, max=200),
                )
            )

        Customer.objects.bulk_create(customers)

        self.stdout.write(
            self.style.SUCCESS(f"✅  Created {count} customers.")
        )
