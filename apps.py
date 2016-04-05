__author__ = 'Dominic Fitzgerald'
from django.apps import AppConfig


class MahoganyAppConfig(AppConfig):
    name = 'mahogany_theme'
    verbose_name = 'Mahogany'

    def ready(self):
        import mahogany_theme.defaults
