from django.contrib.gis.db import models
from taggit.managers import TaggableManager
import datetime


class Household(models.Model):
    name = models.CharField(max_length=100, blank=False)
    street_address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE, blank=False)
    notes = models.TextField(blank=True)


class Neighborhood(models.Model):
    name = models.CharField(max_length=100, blank=False)
    location = models.PointField(blank=False)


class Person(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    ]

    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    household = models.ForeignKey('Household', on_delete=models.CASCADE, blank=False)
    birthdate = models.DateField(blank=True)
    notes = models.TextField(blank=True)
    is_me = models.BooleanField(default=False, blank=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=MALE, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Relationship(models.Model):

    class Category(models.IntegerChoices):
        PARENT = 1
        CHILD = 2
        GRANDPARENT = 3
        GRANDCHILD = 4
        STEPCHILD = 5
        STEPPARENT = 6
        COWORKER = 7
        FRIEND = 8
        CLASSMATE = 9

    person = models.ForeignKey('Person', on_delete=models.CASCADE, blank=False, related_name='related_from_persons')
    related_person = models.ForeignKey('Person', on_delete=models.CASCADE, blank=False, related_name='related_to_persons')
    relationship_category = models.IntegerField(choices=Category.choices, default=Category.FRIEND, blank=False)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Interaction(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='interacted_by_persons')
    interacted_person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='interacted_with_persons')
    notes = models.TextField(blank=True)
    tags = TaggableManager()
    approximate_location = models.PointField(blank=True)
    occurred_at = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
