from django.shortcuts import render
from .models import Note
from django.views.generic import ListView, CreateView, DetailView


class NoteListView(ListView):

    # set model
    model = Note

    def get_queryset(self):

        # filter tags if provided
        if 'tag' in self.kwargs:
            return Note.objects.filter(tags__slug__in=[self.kwargs['tag']])
        else:
            return Note.objects.all()


class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'slug', 'content', 'tags']
    success_url = "/notes/{slug}/"
    ordering = ['-updated_on']


class NoteDetailView(DetailView):
    model = Note

