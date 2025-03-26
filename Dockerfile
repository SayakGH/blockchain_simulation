FROM python:3.9-slim

WORKDIR /app

COPY . /app/
COPY . /Readme.md/

CMD ["python3", "main.py"]