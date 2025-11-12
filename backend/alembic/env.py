from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from asyncio import run as asyncio_run
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
import os
import sys
from pathlib import Path

from app.config import Settings
from app.db import Base

config = context.config
settings = Settings(
    db_url=os.environ.get("DATABASE_URL"),
    db_password=os.environ.get("POSTGRES_PASSWORD"),
)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

if "DATABASE_URL" in os.environ:
    config.set_main_option("sqlalchemy.url", os.environ["DATABASE_URL"])

target_metadata = Base.metadata

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_offline() -> None:
    url =settings.db_url
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    db_url = settings.db_url
    connectable = create_async_engine(
        db_url,
        poolclass=pool.NullPool,      
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio_run(run_migrations_online())
