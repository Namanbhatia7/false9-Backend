import socketio

class Auction(socketio.AsyncNamespace):
    def on_connect(self, sid, environ):
        print('connect Auction namespace ', sid)

    def on_disconnect(self, sid):
        print('disconnect ', sid)

    async def on_myevent(self, sid, data):
        print("Bhyi my event")
        await self.emit('my_response', data)
