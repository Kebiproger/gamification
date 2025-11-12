from fastapi import APIRouter,Depends,HTTPException,status
from typing import Annotated
from ..schemas.user import UserRead,UserCreate,UserBase
from ..models.user import User
from ..services.user_service import UserService
from ..repositories.user_repository import UserRepository
from ..db import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/user",tags=["User's router"])

session = Annotated[AsyncSession, Depends(get_async_session)]
def get_current_user_mock(session: Annotated[AsyncSession,Depends(get_async_session)]):
    user = session.get(User,1)
    if not user:
        raise HTTPException(status_code=401,detail="Mock user not found")
    return user

def get_user_service(session: Annotated[AsyncSession,Depends(get_async_session)]):
    repo = UserRepository(session)
    return UserService(repo)

@router.post("/register",response_model=UserRead)
async def handle_registration(user_data:UserCreate,user_service:Annotated[UserService,Depends(get_user_service)]):
    return user_service.register_user(user_data)

@router.post("/action/execute",response_model=UserRead)
async def handle_action_execution(current_user:Annotated[User,Depends(get_async_session)],user_service:Annotated[UserService,Depends(get_user_service)]):
    return user_service.perform_action(user_id=current_user.id)