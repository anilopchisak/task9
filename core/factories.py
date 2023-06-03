from faker import Factory
import factory
from core import models

factory_ru =Factory.create('ru-Ru')

class Department(factory.django.DjangoModelFactory):
    name = factory_ru.word()

    class Meta:
        model = models.Department

class Position(factory.django.DjangoModelFactory):
    name = factory_ru.word()

    class Meta:
        model = models.Position

class Worker(factory.django.DjangoModelFactory):
    name = factory_ru.word()
    surname = factory_ru.word()
    depart = factory.SubFactory(Department)
    position = factory.SubFactory(Position)
    phone = factory_ru.phone_number()
    email = factory_ru.email()
    photo = factory_ru.image()
    kpi = factory_ru.random_number()

    class Meta:
        model = models.Worker
