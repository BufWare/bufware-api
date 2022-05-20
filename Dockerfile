FROM python:3.9
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./api /app/api

COPY ./migrations /app/migrations
COPY ./alembic.ini /app/alembic.ini

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]
