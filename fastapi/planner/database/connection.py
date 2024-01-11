from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional, Any, List

from models.events import Event
from models.users import User


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        
        await init_beanie(
            database=client.db_name,
            document_models=[Event, User],
        )

    model_config = SettingsConfigDict(
        env_fil =".env"
    )


class Database:
    def __init__(self, model) -> None:
        self.model = model
    
    async def save(self, document) -> None:
        await self.model.insert_one(document)
        return
    
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False
    
    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs
    
    async def update(
        self,
        id: PydanticObjectId,
        body: BaseModel,
    ):
        doc = await self.get(id)
        if not doc:
            return False
        
        dic_body = body.model_dump(exclude_unset=True)
        await doc.update({"$set": dic_body})
        return doc
    
    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        
        await doc.delete()
        return True