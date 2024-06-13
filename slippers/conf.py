from typing import List, Literal

from django.conf import settings as django_settings


class Settings:
    @property
    def SLIPPERS_RUNTIME_TYPE_CHECKING(self) -> bool:
        """Enable runtime type checking of props"""
        return getattr(django_settings, "SLIPPERS_RUNTIME_TYPE_CHECKING", django_settings.DEBUG)  # type: ignore

    @property
    def SLIPPERS_CORE_COMPONENT_ATTRS(self) -> str:
        """Core component allowed attributes

        By default, return the common HTMX attributes & id
        """
        return getattr(
            django_settings,
            "SLIPPERS_CORE_COMPONENT_ATTRS",
            "id hx-get hx-post hx-on hx-push-url hx-select hx-select-oob hx-swap "
            "hx-swap-oob hx-target hx-trigger hx-vals"
        )

    @property
    def SLIPPERS_OPEN_TAG_PREFIX(self) -> bool:
        """Prefix for component opening tags"""
        return getattr(django_settings, "SLIPPERS_OPEN_TAG_PREFIX", "qr-")

    @property
    def SLIPPERS_CLOSE_TAG_PREFIX(self) -> bool:
        """Prefix for component closing tags"""
        return getattr(django_settings, "SLIPPERS_CLOSE_TAG_PREFIX", "end_qr-")

    @property
    def SLIPPERS_TYPE_CHECKING_OUTPUT(
        self,
    ) -> List[Literal["console", "overlay"]]:
        """Where to output type checking errors"""
        return getattr(
            django_settings,
            "SLIPPERS_TYPE_CHECKING_OUTPUT",
            ["console", "overlay"],
        )


settings = Settings()
