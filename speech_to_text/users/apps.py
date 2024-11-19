import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "speech_to_text.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import speech_to_text.users.signals  # noqa: F401
