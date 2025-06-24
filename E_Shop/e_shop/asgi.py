import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_shop.settings')  # lowercase
application = get_asgi_application()