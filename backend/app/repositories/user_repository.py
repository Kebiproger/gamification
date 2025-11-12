from sqlalchemy.ext.asyncio import AsyncSession
from ..models.user import User
from ..schemas.user import UserCreate

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user_data):
        db_user=UserCreate.model_validate(user_data)
        await self.session.add(db_user)
        await self.session.commit()
        await self.session.refresh(db_user)
        return db_user
    
    def get_user_by_id(self,user_id:int):
        return self.session.get(User,user_id)
    
    def get_users_all(self,start: int,limit: int):
        return self.session.all
    
    async def update_user(self, user: User):
        await self.session.add(User)
        await self.session.commit()
        await self.session.refresh(User)
        return user