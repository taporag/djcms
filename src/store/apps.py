from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class StoreConfig(AppConfig):
    name = 'store'
    verbose_name = _('stores')

    def ready(self):
        import store.signals