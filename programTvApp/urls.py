from django.urls import path     
from . import views
urlpatterns = [
        path('', views.shows),
        path('shows', views.shows),
        path('shows/new', views.show_form),
        path('shows/add_show', views.add_show),
        path('shows/<id>/edit', views.edit), 
        path('shows/<id>', views.description), 
]