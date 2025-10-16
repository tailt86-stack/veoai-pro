# Build giao diện React trước
FROM node:18 AS frontend
WORKDIR /app/frontend
COPY frontend/ .
RUN npm install && npm run build || echo "skip build"

# Chạy backend Python FastAPI
FROM python:3.11
WORKDIR /app
COPY backend/ ./backend/
COPY --from=frontend /app/frontend ./frontend
RUN pip install -r backend/requirements.txt
EXPOSE 10000
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-10000}"]
