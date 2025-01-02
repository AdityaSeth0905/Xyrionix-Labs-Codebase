import os
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from .fastapi_app import app as fastapi_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

django_app = get_asgi_application()

application = FastAPI()

application.mount("/django", WSGIMiddleware(django_app))
application.mount("/api", fastapi_app)
