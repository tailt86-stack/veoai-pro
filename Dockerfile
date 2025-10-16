# Build giao diện React (frontend)
FROM node:18 AS frontend
WORKDIR /app/frontend
COPY frontend/ .
RUN echo "skip build"

# Chạy backend FastAPI
FROM python:3.11
WORKDIR /app
COPY backend/ ./backend
COPY --from=frontend /app/frontend ./frontend
RUN pip install -r backend/requirements.txt
EXPOSE 10000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "10000"]
