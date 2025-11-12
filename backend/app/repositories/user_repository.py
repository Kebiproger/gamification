from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..models.user import User
from ..schemas.user import UserCreate

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user_data: UserCreate):
        db_user=User(**user_data.model_dump())
        self.session.add(db_user)
        await self.session.commit()
        await self.session.refresh(db_user)
        return db_user
    
    async def get_user_by_id(self,user_id:int):
        return await self.session.get(User,user_id)
    
    async def update_user(self, user: User):
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def get_users_all(self,start: int,limit: int):
        result = await self.session.execute(select(User).offset(start).limit(limit))
        return result.scalars().all()