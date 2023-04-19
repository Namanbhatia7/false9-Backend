import socketio
from app.socket_server.auction_events import Auction

# create a Socket.IO server
sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=["http://localhost:3001"],
    logger=True
)

sio.register_namespace(Auction("/auction"))

# wrap with ASGI application
sio_app = socketio.ASGIApp(
    socketio_server=sio
)

