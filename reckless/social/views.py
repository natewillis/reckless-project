from django.shortcuts import render
from .models import Household, Person, Neighborhood, Interaction, Relationship
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.db.models import Q

def index(request):

    context = {
        'households': Household.objects.all(),
        'neighborhoods': Neighborhood.objects.all(),
        'interactions': Interaction.objects.order_by('-created_at'),
        'interaction_tags': Interaction.tags.most_common(),
    }

    return render(request, 'social/index.html', context)


class HouseholdListView(ListView):

    # set model
    model = Household
    ordering = ['name']


class HouseholdDetailView(DetailView):

    # set model
    model = Household

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        household = self.object
        people = household.people.all()

        relationships = []
        for person in people:
            relationships.extend(person.related_from_persons.all())
            relationships.extend(person.related_to_persons.all())

        context['relationships'] = relationships
        return context


class HouseholdUpdateView(LoginRequiredMixin, UpdateView):
    model = Household
    fields = [
        'name', 'street_address', 'city',
        'state', 'zip_code', 'neighborhood',
        'notes'
    ]
    success_url = "/household/{pk}/"
    login_url = '/admin/'


class HouseholdCreateView(LoginRequiredMixin, CreateView):
    model = Household
    fields = [
        'name', 'street_address', 'city',
        'state', 'zip_code', 'neighborhood',
        'notes'
    ]
    login_url = '/admin/'

    def get_success_url(self):
        return reverse('social:household-detail', kwargs={'pk': self.object.id})



class PersonDetailView(DetailView):

    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        person = self.get_object()
        interactions = Interaction.objects.filter(Q(person=person) | Q(interacted_person=person))
        context['interactions'] = interactions
        return context


class PersonListView(ListView):
    # set model
    model = Person
    ordering = ['last_name', 'first_name']


class PersonCreateView(LoginRequiredMixin, CreateView):
    model = Person
    fields = [
        'first_name', 'last_name', 'household',
        'birthdate', 'is_me', 'sex',
        'notes'
    ]
    login_url = '/admin/'

    def get_initial(self):
        household_pk = self.kwargs.get('household_pk')
        if household_pk is None:
            initial = {}
        else:
            initial = {'household': household_pk}
        return initial

    def get_success_url(self):
        return reverse('social:person-detail', kwargs={'pk': self.object.id})


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = Person
    fields = [
        'first_name', 'last_name', 'household',
        'birthdate', 'is_me', 'sex',
        'notes'
    ]
    success_url = "/person/list/"
    login_url = '/admin/'

    def get_success_url(self):
        return reverse('social:person-detail', kwargs={'pk': self.object.id})
class NeighborhoodDetailView(DetailView):

    # set model
    model = Neighborhood


class NeighborhoodListView(ListView):

    # set model
    model = Neighborhood
    ordering = ['name']


class NeighborhoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Neighborhood
    fields = [
        'name'
    ]
    success_url = "/neighborhood/all"
    login_url = '/admin/'

    def get_success_url(self):
        return reverse('social:neighborhood-detail', kwargs={'pk': self.object.id})


class NeighborhoodCreateView(LoginRequiredMixin, CreateView):
    model = Neighborhood
    fields = [
        'name'
    ]
    success_url = "/neighborhood/all"
    login_url = '/admin/'

    def get_success_url(self):
        return reverse('social:neighborhood-detail', kwargs={'pk': self.object.id})


class InteractionDetailView(DetailView):

    model = Interaction


class InteractionListView(ListView):

    # set model
    model = Interaction
    ordering = ['-updated_on']

    def get_queryset(self):

        # filter tags if provided
        if 'tag' in self.kwargs:
            return Interaction.objects.filter(tags__slug__in=[self.kwargs['tag']])
        else:
            return Interaction.objects.all()

class InteractionCreateView(LoginRequiredMixin, CreateView):
    model = Interaction
    fields = [
        'person', 'interacted_person', 'notes',
        'tags', 'occurred_at'
    ]
    login_url = '/admin/'

    def get_initial(self):
        me = Person.objects.filter(is_me=True).first()
        interacted_person_pk = self.kwargs.get('interacted_person_pk')

        initial = {}
        if me is not None:
            initial['person'] = me.id
        if interacted_person_pk is not None:
            initial['interacted_person'] = interacted_person_pk

        return initial

    def get_success_url(self):
        return reverse('social:interaction-detail', kwargs={'pk': self.object.id})

class RelationshipDetailView(DetailView):

    # set model
    model = Relationship

class RelationshipCreateView(LoginRequiredMixin, CreateView):
    model = Relationship
    fields = [
        'person', 'related_person', 'relationship_category', 'notes'
    ]
    success_url = ""
    login_url = '/admin/'

    def get_success_url(self):
        return reverse('social:relationship-detail', kwargs={'pk': self.object.id})

