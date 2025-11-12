from pydantic import  Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url: str = Field(..., env="DATABASE_URL")
    db_password: str = Field(..., env="DATABASE_PASSWORD")
    db_host: str = Field("localhost", env="DATABASE_HOST")
    db_port: int = Field(5432, env="DATABASE_PORT")
    class Config:
        env_file = ".env"
