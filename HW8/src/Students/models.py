from django.db import models
from faker import Faker

class Student(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True)
    grade = models.PositiveSmallIntegerField(default=0, null=True)
    birth_date = models.DateField(null=True)

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            student = Student(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                birth_date=faker.date_of_birth(minimum_age=14, maximum_age=60),
            )
            student.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} ({self.pk})"
