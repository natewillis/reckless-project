from django.shortcuts import render
from .models import Note
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class NoteListView(ListView):

    # set model
    model = Note
    ordering = ['-updated_on']

    def get_queryset(self):

        # filter tags if provided
        if 'tag' in self.kwargs:
            return Note.objects.filter(tags__slug__in=[self.kwargs['tag']])
        else:
            return Note.objects.all()


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'slug', 'content', 'tags', 'author']
    success_url = "/notes/{slug}/"
    login_url = '/admin/'

    def get_initial(self):
        initial = {'author': self.request.user}
        return initial


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'slug', 'content', 'tags', 'author']
    success_url = "/notes/{slug}/"
    login_url = '/admin/'


class NoteDetailView(DetailView):
    model = Note

