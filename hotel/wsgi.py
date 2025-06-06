import os
from dotenv import load_dotenv  # .env uchun
from django.core.wsgi import get_wsgi_application

# .env faylni o‘qish
load_dotenv()

# Django sozlamalarini ko‘rsatish
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel.settings')

application = get_wsgi_application()
