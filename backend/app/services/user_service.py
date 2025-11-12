from ..repositories.user_repository import UserRepository
from ..schemas.user import UserCreate,UserRead
from fastapi import HTTPException, status

class UserService:
    def __init__(self, user_repo:UserRepository):
        self.repo = user_repo

    async def register_user(self, user_data:UserCreate):
        db_user = self.repo.create_user(user_data)
        return await UserRead.model_validate(db_user)
    
    def perform_action(self, user_id:int):
        user = self.repo.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
        POINTS_PER_ACTION=100
        user.score += POINTS_PER_ACTION
        updated_user = self.repo.update_user(user)
        return UserRead.model_validate(updated_user)