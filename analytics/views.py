from django.db.models import Count
from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator

from analytics.models import Event


def all_events(request: HttpRequest):
    events = Event.objects.all()

    return render(
        request=request,
        template_name="analytics/all_events.html",
        context={"all_events": events}
        )


def events_offset_paginated(request: HttpRequest):
    events = Event.objects.all().order_by("id")

    paginated = Paginator(events, per_page=settings.EVENT_PER_PAGE)
    page = request.GET.get("page", 1)
    events = paginated.get_page(page)
    
    return render(
        request=request,
        template_name="analytics/events_offset_paginated.html",
        context={"events": events}
        )


def events_with_related_users(request: HttpRequest):
    events = Event.objects.select_related("user")

    paginated = Paginator(events, per_page=settings.EVENT_PER_PAGE)
    page = request.GET.get("page", 1)
    events = paginated.get_page(page)

    return render(
        request=request,
        template_name="analytics/paginated_events_with_users.html",
        context={"events": events}
        )


def count_events_users(request: HttpRequest):
    events = Event.objects.select_related("user").annotate(users_count=Count("user"))

    return render(
        request=request,
        template_name="analytics/count_events_users.html",
        context={"events": events}
        )
