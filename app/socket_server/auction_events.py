import socketio

class Auction(socketio.AsyncNamespace):
    def on_connect(self, sid, environ):
        print('connect Auction namespace ', sid)

    def on_disconnect(self, sid):
        print('disconnect ', sid)

    async def on_join_room(self, sid, data):
        print(f"Bhyi my event {data}")
        self.enter_room(sid, data["roomId"])
