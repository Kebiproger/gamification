from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from app.config import Settings
from sqlalchemy.orm import declarative_base
from collections.abc import AsyncGenerator

settings = Settings() # Инициализация настроек из config.py создавая обьект

engine = create_async_engine(
    settings.db_url,
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
