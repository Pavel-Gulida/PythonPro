from django.db import models
from faker import Faker

class Teachers(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True)
    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    phone_number = models.CharField(max_length=120, null=True, blank=True)

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            teacher = Teachers(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                birth_date=faker.date_of_birth(minimum_age=14, maximum_age=60),
                address = faker.address(),
                phone_number = faker.phone_number()
            )
            teacher.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} ({self.pk})"