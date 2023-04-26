from typing import List, Dict, Any
from app.utils.datatype_models import UserDetails


user_list: List[UserDetails] = []

def add_users(payload: UserDetails):
    global user_list
    user_list.append(
        UserDetails(
            room_id=payload.room_id,
            username=payload.username,
            user_id=payload.user_id
        )
    )

def get_users_in_room(room_id: str):
    global user_list
    return len([user for user in user_list if user.room_id == room_id])

def remove_user_from_room(user_id: str):
    global user_list
    if user_list:
        user_list = [user for user in user_list if user.user_id != user_id]
        print(user_list)
    


