from django.urls import path
from . import views

# URL patterns for the landing app
urlpatterns = [
    path('', views.index, name='index'),  # Route for the landing page
]