from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator

from analytics.models import Event


def all_events(request: HttpRequest):
    all_events = Event.objects.all()

    return render(request=request, template_name="analytics/all_events.html", context={"all_events": all_events})


def events_offset_paginated(request: HttpRequest):
    all_events = Event.objects.all().order_by("id")

    paginated = Paginator(all_events, per_page=settings.EVENT_PER_PAGE)
    page = request.GET.get("page", 1)
    events = paginated.get_page(page)
    
    return render(
        request=request,
        template_name="events_offset_paginated.html",
        context={"events": events}
        )

