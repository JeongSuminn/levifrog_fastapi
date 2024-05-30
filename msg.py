from fastapi import APIRouter, Path
from model import Msg
from datetime import datetime

msg_router = APIRouter()

msg_list = []
msg_counter = 0
current_time = 0

@msg_router.post("/msg")
async def add_msg(msg: Msg) -> dict:
    global msg_counter
    msg.id = msg_counter = msg_counter + 1
    msg_list.append(msg)
    current_time = datetime.now()
    msg.datetime = current_time.strftime('%Y-%m-%d %H:%M:%S')
    return {
        "msg" : "msg added successfully"
    }
    
@msg_router.get("/msg")
async def retrieve_msgs() -> dict:
    return {
        "msgs" : msg_list
    }
    
@msg_router.get("/msg/{msg_id}")
async def get_single_msg(msg_id: int = Path(..., title = "the ID of the msg to retrieve")) -> dict:
    for msg in msg_list:
        if msg.id == msg_id:
            return { "msg" : msg}
    return {"msg" : "msg with supplied ID doesn't exist"}

@msg_router.delete("/msg/{msg_id}")
async def delete_msg(msg_id: int = Path(..., title = "the ID of the msg to retrieve")) -> dict:
    for index, msg in enumerate(msg_list):
        if msg.id == msg_id:
            del msg_list[index]
            return { "msg" : "msg with ID {msg_id} deleted successfully"}
    return {"msg" : "msg with supplied ID doesn't exist"}