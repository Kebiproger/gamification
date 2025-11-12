#!/bin/bash

# Выходим, если любая команда завершится с ошибкой
set -e

# 1. Ждем, пока Postgres будет готов
# Мы используем переменные окружения, которые Docker Compose передает в контейнер db
# Но нам нужен хост 'db' (имя сервиса)
echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "Database started"

# 2. Применяем миграции Alembic
# Выполняем команду alembic изнутри контейнера
echo "Running database migrations..."
alembic upgrade head

# 3. Запускаем Uvicorn (основную команду)
# $@ позволяет передать любые аргументы (например, CMD из Dockerfile)
exec "$@"