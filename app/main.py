from fastapi import FastAPI
# from sockets import sio_app
from app.socket_server.sockets import sio_app


app = FastAPI()


@app.get("/users")
async def root():
    return {"message": "Hello World"}

app.mount("/", app=sio_app)