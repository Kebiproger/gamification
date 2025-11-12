from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from .config import Settings
from sqlalchemy.orm import declarative_base
import os 

settings = Settings(database_url=os.environ.get("DATABASE_URL")) # Инициализация настроек из config.py создавая обьект

engine = create_async_engine(
    settings.database_url,
    echo=True,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True, # Проверяет соединение перед использованием из пула    
)

async_session_factory = async_sessionmaker(
    bind=engine, # Привязка к движку
    expire_on_commit=False, # Отключение истечения срока действия объектов после фиксации транзакции
    class_=AsyncSession
)

Base = declarative_base()

async def get_async_session():
    async with async_session_factory() as session:
        yield session
