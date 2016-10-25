"""
WSGI config for pressp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/

except ImportError:
    print("uwsgidecorators not found. Cron and timers are disabled")

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pressp.settings")

application = get_wsgi_application()

os.environ["CELERY_LOADER"] = "django"
























































