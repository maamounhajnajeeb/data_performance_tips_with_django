from django.urls import path

from analytics import views


app_name = "analytics_app"

urlpatterns = [
    path("all_events/", views.all_events, name="all_events"),
    path("count_events_users/", views.count_events_users, name="count_events_users"),
    path("events_offset_paginated/", views.events_offset_paginated, name="events_offset_paginated"),
    path("events_with_related_users/", views.events_with_related_users, name="events_with_related_users"),
]
