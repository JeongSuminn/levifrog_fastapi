from fastapi import APIRouter, Path
from model import Todo
from datetime import datetime

todo_router = APIRouter()

todo_list = []
todo_counter = 0
current_time = 0

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    global todo_counter
    todo.id = todo_counter = todo_counter + 1
    todo_list.append(todo)
    current_time = datetime.now()
    todo.datetime = current_time.strftime('%Y-%m-%d %H:%M:%S')
    return {
        "msg" : "todo added successfully"
    }
    
@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
        "todos" : todo_list
    }
    
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title = "the ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return { "todo" : todo}
    return {"msg" : "todo with supplied ID doesn't exist"}

@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int = Path(..., title = "the ID of the todo to retrieve")) -> dict:
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            del todo_list[index]
            return { "msg" : "Todo with ID {todo_id} deleted successfully"}
    return {"msg" : "todo with supplied ID doesn't exist"}