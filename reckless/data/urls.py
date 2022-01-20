from data.views import SourceListView, SourceDetailView
from django.urls import path

app_name = 'data'
urlpatterns = [
    path('', SourceListView.as_view(), name='list'),
    path('<slug:slug>/', SourceDetailView.as_view(), name='detail'),
]
