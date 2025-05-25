from django.urls import path
from .views import DocumentListView, DocumentDetailView

urlpatterns = [
    path('', DocumentListView.as_view(), name='document-list'),
    path('<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
] 