import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_framework_tutorial.settings')

application = get_asgi_application()
