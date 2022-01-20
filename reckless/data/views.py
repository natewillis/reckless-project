from .models import Source
from django.views.generic import ListView, DetailView


class SourceListView(ListView):

    # set model
    model = Source
    ordering = ['title']


class SourceDetailView(DetailView):
    model = Source