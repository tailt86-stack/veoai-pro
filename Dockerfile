# Dùng Python 3.11 để chạy backend FastAPI
FROM python:3.11-slim

# Tạo thư mục làm việc trong container
WORKDIR /app

# Copy mã nguồn và file requirements
COPY backend/ ./backend
COPY requirements.txt .

# Cài đặt thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Mở port 10000 để Render truy cập
EXPOSE 10000

# Chạy ứng dụng FastAPI bằng Uvicorn
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "10000"]
