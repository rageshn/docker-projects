FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

WORKDIR /app/src/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081", "--reload"]