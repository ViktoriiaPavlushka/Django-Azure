
import os

from django.core.wsgi import get_wsgi_application
settings_module = "djangoCinema.deployment" if 'ПолітехCinema_HOST' in os.environ else "djangoCinema.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()
