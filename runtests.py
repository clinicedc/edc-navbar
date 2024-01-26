#!/usr/bin/env python
import logging
from pathlib import Path

import arrow
from dateutil.relativedelta import relativedelta
from edc_test_utils import DefaultTestSettings, func_main

app_name = "edc_navbar"
base_dir = Path(__file__).absolute().parent

project_settings = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    SILENCED_SYSTEM_CHECKS=["sites.E101", "edc_navbar.E003"],
    ETC_DIR=str(base_dir / app_name / "tests" / "etc"),
    ADVERSE_EVENT_APP_LABEL="adverse_event_app",
    ADVERSE_EVENT_ADMIN_SITE="adverse_event_app_admin",
    EDC_PROTOCOL_STUDY_OPEN_DATETIME=arrow.utcnow().floor("hour") - relativedelta(years=2),
    EDC_PROTOCOL_STUDY_CLOSE_DATETIME=arrow.utcnow().ceil("hour") + relativedelta(years=2),
    EDC_NAVBAR_DEFAULT=app_name,
    EDC_AUTH_CODENAMES_WARN_ONLY=True,
    EDC_SITES_REGISTER_DEFAULT=True,
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "multisite",
        "django_crypto_fields.apps.AppConfig",
        "django_revision.apps.AppConfig",
        "edc_action_item.apps.AppConfig",
        "edc_adverse_event.apps.AppConfig",
        "edc_appointment.apps.AppConfig",
        "edc_auth.apps.AppConfig",
        "edc_dashboard.apps.AppConfig",
        "edc_data_manager.apps.AppConfig",
        "edc_export.apps.AppConfig",
        "edc_facility.apps.AppConfig",
        "edc_form_runners.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_list_data.apps.AppConfig",
        "edc_listboard.apps.AppConfig",
        "edc_metadata.apps.AppConfig",
        "edc_model_form.apps.AppConfig",
        "edc_navbar.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_pharmacy.apps.AppConfig",
        "edc_randomization.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_review_dashboard.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_subject_dashboard.apps.AppConfig",
        "edc_timepoint.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        "edc_visit_tracking.apps.AppConfig",
        "adverse_event_app.apps.AppConfig",
        "edc_appconfig.apps.AppConfig",
    ],
    add_dashboard_middleware=True,
    use_test_urls=True,
).settings


def main():
    func_main(project_settings, *[f"{app_name}.tests"])


if __name__ == "__main__":
    logging.basicConfig()
    main()
