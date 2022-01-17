from notes.views import NoteListView, NoteCreateView, NoteDetailView
from django.urls import path

app_name = 'notes'
urlpatterns = [
    path('', NoteListView.as_view(), name='list'),
    path('add/', NoteCreateView.as_view(), name='add'),
    path('<slug:slug>/', NoteDetailView.as_view(), name='detail'),
    path('tag/<slug:tag>/', NoteListView.as_view(), name='tag-list')
]
