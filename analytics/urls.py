from django.urls import path

from analytics import views


app_name = "analytics_app"

urlpatterns = [
    path("all_events/", views.all_events, name="all_events"),
    path("events_offset_paginated/", views.events_offset_paginated, name="events_offset_paginated"),
]
