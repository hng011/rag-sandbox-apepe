FROM python:3.12.3-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /sandboxragapepe

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY /app ./app
COPY /config ./config

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app/Main.py", "--server.port=8501", "--server.address=0.0.0.0"]