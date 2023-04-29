from typing import List, Dict, Any
from app.utils.datatype_models import UserDetails


class UserManager():
    user_list: List[UserDetails] = []

    @classmethod
    def add_users(cls, payload: UserDetails):
        cls.user_list.append(
            UserDetails(
                room_id=payload.room_id,
                username=payload.username,
                user_id=payload.user_id
            )
        )

    def get_users_in_room(self, room_id: str):
        room_data_list = [user.json() for user in self.user_list if user.room_id == room_id]
        return room_data_list

    @classmethod
    def remove_user_from_room(cls, user_id: str):
        if cls.user_list:
            cls.user_list = [user for user in cls.user_list if user.user_id != user_id]


user_manager = UserManager()