from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def __str__(self) -> str:
        return f"user id: {self.id}, user first name: {self.first_name}"
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

        ordering = ["id"]
