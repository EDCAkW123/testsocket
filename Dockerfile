# Используем базовый образ Python
FROM python:3.13-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порты 3000 и 5500
EXPOSE 3000 5500

# Запускаем приложение
CMD ["python", "app.py"]
