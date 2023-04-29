from typing import Dict, Any

import socketio
from app.user_manager.user_manager import user_manager
from app.utils.datatype_models import UserDetails

class Auction(socketio.AsyncNamespace):
    def on_connect(self, sid, environ):
        print('connect Auction namespace ', sid)

    # Resolve user_list as global state problem
    def on_disconnect(self, sid):
        print('disconnect ', sid)
        user_manager.remove_user_from_room(sid)

    async def on_join_room(self, sid, data):
        room_data = UserDetails(
            room_id = data["roomId"],
            username = data["username"],
            user_id = sid
        )

        user_manager.add_users(room_data)
        users_in_room_data = user_manager.get_users_in_room(room_data.room_id)

        payload: Dict[str, Any] = {
            "room_id": data["roomId"],
            "room_data": users_in_room_data,
            "error": ""
        }

        if len(users_in_room_data) <= 2:
            try:
                self.enter_room(sid, data["roomId"])
            except:
                print("Error while joining the room")
                user_manager.remove_user_from_room(sid)
                payload["error"] = "Something went wrong"
            else:
                await self.emit("gamespace", payload, room=room_data.room_id)
        else:
            payload["error"] = f"{room_data.room_id} room is Full "
            await self.emit("gamespace", payload, room=room_data.room_id, to=sid)

        print("Done")
