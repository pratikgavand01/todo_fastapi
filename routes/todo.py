from fastapi import APIRouter
import all_routes
from model.pydantic_model import Todo
import operations.to_do as db

todo_route = APIRouter()


@todo_route.post(all_routes.todo_create)
def new_todo(doc: Todo):
    data=doc.model_dump()
    print(data["todo"])
    res = db.create_todo(data["todo"])
    return res

@todo_route.get(all_routes.todo_all)
def all_todos():
    res = db.get_all_todos()
    return res

@todo_route.get(all_routes.todo_one)
def get_todo(id: int):
    res = db.get_todo(id)
    return res

    
@todo_route.put(all_routes.todo_update)
def update_todo(id: int, doc: Todo):
    data = doc.model_dump()
    title: str = data['todo']
    res = db.update_todo(id, title)
    return res

        
@todo_route.delete(all_routes.todo_delete)
def delete_todo(id: int):
    res = db.delete_todo(id)
    return res