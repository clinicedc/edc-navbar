from django.apps import apps as django_apps
from django.core.checks import CheckMessage, Error
from django.urls import NoReverseMatch, reverse

from edc_navbar import site_navbars


def edc_navbar_checks(app_configs, **kwargs) -> list[CheckMessage]:
    errors = []

    for navbar_name, navbar in site_navbars.registry.items():
        for navbar_item in navbar.navbar_items:
            try:
                app_label, codename = navbar_item.codename.split(".")
            except ValueError:
                errors.append(
                    Error(
                        f"Invalid codename. Got '{navbar_item.codename}'."
                        "See {repr(navbar_item)}.",
                        id="edc_navbar.E001",
                    )
                )
            else:
                if app_label not in [a.name for a in django_apps.get_app_configs()]:
                    msg = (
                        f"Invalid app_label in codename. Expected format "
                        f"'<app_label>.<some_codename>'. Got {navbar_item.codename}. "
                        f"See {repr(navbar_item)}."
                    )
                    errors.append(Error(msg, id="edc_navbar.E002"))
            try:
                reverse(navbar_item.url_name)
            except NoReverseMatch:
                errors.append(
                    Error(
                        f"Invalid url_name. Got '{navbar_item.url_name}'. "
                        "See {repr(navbar_item)}.",
                        id="edc_navbar.E003",
                    )
                )

    return errors
