from django.urls import path
from . import views

app_name = 'tierlist'

urlpatterns = [
    path('tierlist/', views.tierlist_view, name='tierlist'),
]