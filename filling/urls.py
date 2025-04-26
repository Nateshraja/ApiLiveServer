from django.urls import path
from . import views

urlpatterns = [
    path('file-entry/', views.create_filing_entry, name='create_filing_entry'),
]
