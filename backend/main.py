from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
# Mount thư mục frontend để truy cập file HTML
app.mount("/frontend", StaticFiles(directory="backend/backend/frontend"), name="frontend")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>🚀 VeoAI-Pro is running successfully!</h1><p>This is a test FastAPI app.</p>"
from fastapi import Request
from pydantic import BaseModel

class ScriptRequest(BaseModel):
    script: str

@app.post("/api/generate")
async def generate_video(req: ScriptRequest):
    # Tạm thời mô phỏng tạo video
    # Sau này bạn sẽ thay phần này bằng API của Veo hoặc OpenAI
    return {"url": "https://example.com/fake_video.mp4"}
from fastapi import Request

@app.post("/generate-video")
async def generate_video(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "Không có nội dung")
    # Sau này bạn sẽ tích hợp phần sinh video tại đây
    return {"status": "ok", "message": f"Đang tạo video cho prompt: {prompt}"}
