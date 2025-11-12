from ..repositories.user_repository import UserRepository
from ..schemas.user import UserCreate,UserRead
from fastapi import HTTPException, status

class UserService:
    def __init__(self, user_repo:UserRepository):
        self.repo = user_repo

    async def register_user(self, user_data:UserCreate):
        db_user = await self.repo.create_user(user_data)
        return UserRead.model_validate(db_user.__dict__)
    
    async def perform_action(self, user_id:int):
        user = await self.repo.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
        POINTS_PER_ACTION=100
        user.score += POINTS_PER_ACTION
        updated_user = await self.repo.update_user(user)
        return UserRead.model_validate(updated_user)
    async def get_users_all(self, start:int,limit:int=100):
        return await self.repo.get_users_all(start,limit)