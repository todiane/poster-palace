from django.urls import path
from . import views

app_name = "marketing"

urlpatterns = [
    path("", views.subscription, name="subscription"),
    path("poster_event/", views.poster_event, name="poster_event"),
    path("event_terms/", views.event_terms, name="event_terms"),
]
