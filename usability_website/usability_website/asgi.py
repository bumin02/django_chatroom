import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import room.routing
import message.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "usability_website.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            message.routing.websocket_urlpatterns + room.routing.websocket_urlpatterns
            # room.routing.websocket_urlpatterns + message.routing.websocket_urlpatterns
        )
    )
})