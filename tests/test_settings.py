import sys
from pathlib import Path

from clinicedc_tests.config import DefaultTestSettings, get_installed_apps_for_tests

app_name = "edc_microscopy"
base_dir = Path(__file__).absolute().parent.parent

project_settings = DefaultTestSettings(
    app_name="clinicedc_tests",
    calling_file=__file__,
    BASE_DIR=base_dir,
    ETC_DIR=base_dir / "tests" / "etc",
    DJANGO_CRYPTO_FIELDS_KEY_PATH=base_dir / "tests" / "etc",
    APP_NAME=app_name,
    SILENCED_SYSTEM_CHECKS=[
        "sites.E101",
        "edc_sites.E001",
        "edc_sites.E002",
        "edc_navbar.E003",
        "edc_navbar.E004",
        "edc_consent.E001",
    ],  # The SITE_ID setting must be an integer
    INSTALLED_APPS=[
        *get_installed_apps_for_tests("clinicedc_tests", "edc_microscopy.apps.AppConfig"),
    ],
    add_dashboard_middleware=True,
    add_lab_dashboard_middleware=True,
    DJANGO_REVISION_IGNORE_WORKING_DIR=True,
).settings

for k, v in project_settings.items():
    setattr(sys.modules[__name__], k, v)
