FROM python:3.12-slim

WORKDIR /code

# Копируем только файл с зависимостями
COPY pyproject.toml poetry.lock ./

# Устанавливаем Poetry и зависимости
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root

# Копируем остальной код проекта
COPY . .

# Команда для запуска приложения
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]