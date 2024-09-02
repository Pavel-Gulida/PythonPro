from django.db import models
from faker import Faker

class Group(models.Model):

    number = models.PositiveIntegerField(default=1, null=True)
    group_leader = models.CharField(max_length=120, null=True, blank=True)
    average_score = models.PositiveIntegerField(default=1, null=True)
    count_students = models.PositiveIntegerField(default=1, null=True)
    count_subject = models.PositiveIntegerField(default=1, null=True)
    average_age = models.PositiveIntegerField(default=1, null=True)

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            group = Group(
                number = faker.random_int(min=1),
                group_leader = faker.name(),
                average_score=faker.random_int(min=0,max=100),
                count_students=faker.random_int(min=7, max=40),
                count_subject=faker.random_int(min=5, max=13),
                average_age = faker.random_int(min=18,max=60),
            )
            group.save()
