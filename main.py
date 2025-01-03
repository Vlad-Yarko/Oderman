from My_app import app
from asgiref.wsgi import WsgiToAsgi

asgi_app = WsgiToAsgi(app)

