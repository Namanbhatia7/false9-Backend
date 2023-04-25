from pydantic import BaseModel

class UserDetails(BaseModel):
    user_id: str
    username: str
    room_id: str