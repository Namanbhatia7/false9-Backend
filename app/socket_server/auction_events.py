import socketio

class Auction(socketio.AsyncNamespace):
    def on_connect(self, sid, environ):
        print('connect Auction namespace ', sid)

    def on_disconnect(self, sid):
        print('disconnect ', sid)

    async def on_join_room(self, sid, data):
        self.enter_room(sid, data["roomId"])
        room_data = {
            "room_id": data["roomId"]
        }
        await self.emit("gamespace", room_data, room=data["roomId"])
        print("Done")
