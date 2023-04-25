from typing import List, Dict, Any
from app.utils.datatype_models import UserDetails


user_list: List[UserDetails] = []

def add_users(payload: UserDetails):
    user_list.append(
        UserDetails(
            room_id=payload.room_id,
            username=payload.username,
            user_id=payload.user_id
        )
    )

def get_users_in_room(room_id: str):
    return len([user for user in user_list if user.room_id == room_id])
    


