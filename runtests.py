#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname

app_name = 'edc_navbar'
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=os.path.join(base_dir, app_name, "tests", "etc"),
    EDC_BOOTSTRAP=3,
    EDC_NAVBAR_DEFAULT="edc_navbar",
    INSTALLED_APPS=[
        'django_celery_beat',
        'django_celery_results',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.messages',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        "django_crypto_fields.apps.AppConfig",
        "edc_appointment.apps.AppConfig",
        "edc_consent.apps.AppConfig",
        "edc_protocol.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_identifier.apps.AppConfig",
        'edc_action_item.apps.AppConfig',
        'edc_notification.apps.AppConfig',
        'edc_dashboard.apps.AppConfig',
        'edc_auth.apps.AppConfig',
        'edc_data_manager.apps.AppConfig',
        'edc_export.apps.AppConfig',
        'edc_lab.apps.AppConfig',
        'edc_locator.apps.AppConfig',
        'edc_metadata.apps.AppConfig',
        'edc_pharmacy.apps.AppConfig',
        'edc_sites.apps.AppConfig',
        'edc_navbar.apps.AppConfig',
        'edc_offstudy.apps.AppConfig',
        'edc_visit_schedule.apps.AppConfig',
        'edc_adverse_event.apps.AppConfig',
        'adverse_event_app.apps.AppConfig',
    ],
    add_dashboard_middleware=True,
    use_test_urls=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    failures = DiscoverRunner(failfast=True).run_tests([f'{app_name}.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
