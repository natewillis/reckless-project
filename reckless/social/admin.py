from django.contrib import admin
from .models import Neighborhood, Household, Person, Relationship, Interaction

admin.site.register(Neighborhood)
admin.site.register(Household)
admin.site.register(Person)
admin.site.register(Relationship)
admin.site.register(Interaction)
