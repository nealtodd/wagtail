from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WagtailTestsAppConfig(AppConfig):
    name = "wagtail.tests.testapp"
    label = "tests"
    verbose_name = _("Wagtail tests")
