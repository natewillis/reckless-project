from social.views import HouseholdDetailView, PersonDetailView, index, NeighborhoodDetailView, \
    InteractionDetailView, InteractionListView, HouseholdUpdateView, HouseholdCreateView, \
    PersonCreateView, PersonListView, HouseholdListView, NeighborhoodListView, InteractionCreateView, \
    PersonUpdateView
from django.urls import path

app_name = 'social'
urlpatterns = [
    path('', index, name='index'),
    path('household/<int:pk>/', HouseholdDetailView.as_view(), name='household-detail'),
    path('household/all/', HouseholdListView.as_view(), name='household-list'),
    path('household/update/<int:pk>/', HouseholdUpdateView.as_view(), name='household-update'),
    path('household/create/', HouseholdCreateView.as_view(), name='household-create'),
    path('neighborhood/<int:pk>/', NeighborhoodDetailView.as_view(), name='neighborhood-detail'),
    path('neighborhood/all/', NeighborhoodListView.as_view(), name='neighborhood-list'),
    path('interaction/<int:pk>/', InteractionDetailView.as_view(), name='interaction-detail'),
    path('interactions/tag/<slug:tag>/', InteractionListView.as_view(), name='interaction-tag-list'),
    path('interaction/create/', InteractionCreateView.as_view(), name='interaction-create'),
    path('interaction/interacted_person/<int:interacted_person_pk>/create/', InteractionCreateView.as_view(), name='interaction-with-interacted-person-create'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
    path('people/', PersonListView.as_view(), name='person-list'),
    path('person/household/<int:household_pk>/create/', PersonCreateView.as_view(), name='person-with-household-create'),
    path('person/create/', PersonCreateView.as_view(), name='person-create'),
    path('person/update/<int:pk>/', PersonUpdateView.as_view(), name='person-update'),
]