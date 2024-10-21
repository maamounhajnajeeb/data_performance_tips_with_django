from typing import Literal

from django.http import HttpRequest
from django.db.models import QuerySet


class PaginatedSessions:

    def __init__(
            self, request: HttpRequest, queryset: QuerySet, cursor: Literal["pre", "nxt"], limit: int
            ) -> None:
        # set attrs from request object
        self.user, self.session = request.user, request.session

        # set the queryset and others
        self.queryset, self.limit, self.cursor = queryset, limit, cursor

    def get_paginated_queryset(self):
        pass
    
    def manage_session(self):
        # get the users_pagination_records
        users_session_dict = self.session.get("users_pagination_records")
        if users_session_dict is None:
            self.session["users_pagination_records"] = {}
        
        # the user is new (no session recorded)
        if users_session_dict.get(self.user.id) is None:
            queryset = self.queryset[:self.limit]
            users_session_dict[self.user.id] = {
                "first_item_id": queryset.first().id, "last_item_id": queryset.last().id
                }

        # the user is old and has session
        if users_session_dict.get(self.user.id) is not None:
            if self.cursor == "nxt":
                pass
            
            elif self.cursor == "pre":
                pass
