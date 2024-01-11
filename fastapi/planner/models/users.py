from pydantic import BaseModel, ConfigDict, EmailStr
from typing import List, Optional
from beanie import Document, Link

from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    username: str
    events: Optional[List[Event]] = None

    model_config = ConfigDict(
        json_schema_extra={
            "Examples": [
                {
                    "email": "fastapi@packt.com",
                    "password": "strong!!!",
                    "username": "Lee",
                    "events": [],
                }
            ]
        }
    )


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "Examples": [
                {
                    "email": "fastapi@packt.com",
                    "password": "strong!!!",
                }
            ]
        }
    )
