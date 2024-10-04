from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class Event(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False, blank=False,
        verbose_name=_("Related User")
        )
    learning_event = models.CharField(
        max_length=256,
        null=False, blank=False,
        verbose_name=_("Learning Event")
        )
    event_description = models.TextField(
        blank=False, null=False,
        verbose_name=_("Evenv Description")
        )

    def __str__(self) -> str:
        return f"event id: {self.id}, user id: {self.user.id}, user firstname: {self.user.first_name}"

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
