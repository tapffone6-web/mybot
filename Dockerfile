FROM python:3.9-slim
WORKDIR /app
RUN pip install aiogram==2.25.1
COPY . .
CMD ["python", "bot.py"]
