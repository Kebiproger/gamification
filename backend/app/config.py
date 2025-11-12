from pydantic import  Field
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    db_url: str 
    db_password: str 
    model_config = SettingsConfigDict(
        extra='ignore', # Игнорировать переменные, которых нет в классе (например, POSTGRES_USER)
    )
