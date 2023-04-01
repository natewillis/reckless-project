from django.contrib.gis.db import models
from taggit.managers import TaggableManager
import datetime
from django.core.exceptions import ValidationError

class Household(models.Model):
    name = models.CharField(max_length=100, blank=False)
    street_address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE, blank=False, related_name='households')
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
    def __str__(self):
        return f'{self.name} in {self.neighborhood.name}'


class Neighborhood(models.Model):
    name = models.CharField(max_length=100, blank=False)
    location = models.PointField(null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Person(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    ]

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    f3_name = models.CharField(max_length=100, blank=True)
    household = models.ForeignKey('Household', on_delete=models.CASCADE, blank=False, related_name='people')
    birthdate = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    is_me = models.BooleanField(default=False, blank=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=MALE, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        # Use a list comprehension to filter out blank fields, then join them with spaces
        return ' '.join([name for name in [self.first_name, self.f3_name, self.last_name] if name])

    def clean(self):
        # Check if at least one of first_name, last_name, and f3_name is present
        if not (self.first_name or self.last_name or self.f3_name):
            raise ValidationError('At least one of first_name, last_name, or f3_name must be provided.')

    def save(self, *args, **kwargs):
        self.clean()
        super(Person, self).save(*args, **kwargs)


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
        SPOUSE = 10
        SIGNIFICANT_OTHER = 11
        STUDENT = 12
        TEACHER = 13
        SIBLING = 14

    person = models.ForeignKey('Person', on_delete=models.CASCADE, blank=False, related_name='related_from_persons')
    related_person = models.ForeignKey('Person', on_delete=models.CASCADE, blank=False, related_name='related_to_persons')
    relationship_category = models.IntegerField(choices=Category.choices, default=Category.FRIEND, blank=False)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.related_person} is {self.person}\'s {self.get_relationship_category_display()}'


class Interaction(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='interacted_by_persons')
    interacted_people = models.ManyToManyField('Person', related_name='interacted_with_people')
    notes = models.TextField(blank=True)
    tags = TaggableManager()
    approximate_location = models.PointField(null=True)
    occurred_at = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-occurred_at"]
    def __str__(self):
        interacted_people_list = ", ".join(str(person) for person in self.interacted_people.all())
        return f"{self.person} interacted with {interacted_people_list} on {self.occurred_at} [{self.joined_tags()}]"
    def joined_tags(self):
        return ",".join(self.tags.names())
