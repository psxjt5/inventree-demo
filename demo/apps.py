"""Django config for the demo plugin."""

from django.apps import AppConfig

class demoConfig(AppConfig):
    """Config class for the demo plugin."""

    name = 'demo'

    def ready(self):
        """This function is called whenever the demo plugin is loaded."""
        ...
