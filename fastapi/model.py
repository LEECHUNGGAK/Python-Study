from pydantic import BaseModel

from fastapi import Form

from typing import List, Optional


class Item(BaseModel):
    item: str
    status: str


class Todo(BaseModel):
    id: Optional[int] = None
    item: Item

    @classmethod
    def as_form(
        cls,
        item: str = Form(...),
        status: str = "Backlog",
    ):
        return cls(item={"item": item, "status": status})

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"id": 1, "item": {"item": "Example Schema!", "status": "completed"}}
            ]
        }
    }


class TodoItem(BaseModel):
    item: str

    model_config = {
        "json_schema_extra": {
            "examples": [{"item": "Read the next chapter of the book."}]
        }
    }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "todos": [
                        {"item": "Example schema 1!"},
                        {"item": "Example schema 2!"},
                    ]
                }
            ]
        }
    }
