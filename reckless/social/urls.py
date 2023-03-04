from social.views import HouseholdDetailView, PersonDetailView, index, NeighborhoodDetailView, \
    InteractionDetailView, InteractionListView, HouseholdUpdateView, HouseholdCreateView, \
    PersonCreateView, PersonListView, HouseholdListView, NeighborhoodListView, InteractionCreateView, \
    PersonUpdateView, NeighborhoodUpdateView, NeighborhoodCreateView, RelationshipDetailView, RelationshipCreateView
from django.urls import path

app_name = 'social'
urlpatterns = [
    path('', index, name='index'),
    path('household/<int:pk>/', HouseholdDetailView.as_view(), name='household-detail'),
    path('households/', HouseholdListView.as_view(), name='household-list'),
    path('household/update/<int:pk>/', HouseholdUpdateView.as_view(), name='household-update'),
    path('household/create/', HouseholdCreateView.as_view(), name='household-create'),
    path('neighborhood/<int:pk>/', NeighborhoodDetailView.as_view(), name='neighborhood-detail'),
    path('neighborhoods/', NeighborhoodListView.as_view(), name='neighborhood-list'),
    path('neighborhood/update/<int:pk>/', NeighborhoodUpdateView.as_view(), name='neighborhood-update'),
    path('neighborhood/create/', NeighborhoodCreateView.as_view(), name='neighborhood-create'),
    path('interaction/<int:pk>/', InteractionDetailView.as_view(), name='interaction-detail'),
    path('interactions/', InteractionListView.as_view(), name='interaction-list'),
    path('interactions/tag/<slug:tag>/', InteractionListView.as_view(), name='interaction-tag-list'),
    path('interaction/create/', InteractionCreateView.as_view(), name='interaction-create'),
    path('interaction/interacted_person/<int:interacted_person_pk>/create/', InteractionCreateView.as_view(), name='interaction-with-interacted-person-create'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
    path('people/', PersonListView.as_view(), name='person-list'),
    path('person/household/<int:household_pk>/create/', PersonCreateView.as_view(), name='person-with-household-create'),
    path('person/create/', PersonCreateView.as_view(), name='person-create'),
    path('person/update/<int:pk>/', PersonUpdateView.as_view(), name='person-update'),
    path('relationship/<int:pk>', RelationshipDetailView.as_view(), name='relationship-detail'),
    path('relationship/create/', RelationshipCreateView.as_view(), name='relationship-create'),
    path('relationship/person/<int:person_pk>/create/', RelationshipCreateView.as_view(), name='relationship-with-person-create'),
]
