from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os, json, time

app = FastAPI()

@app.get("/")
def home():
    return {"message": "✅ VeoAI-Pro backend đang chạy tốt!"}

@app.post("/generate-video")
async def generate_video(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")

    # ⚙️ Giả lập quá trình tạo video (bạn sẽ thay bằng API thật sau)
    print(f"🎬 Bắt đầu tạo video cho prompt: {prompt}")
    time.sleep(5)

    # ⚙️ Giả lập link video xuất ra
    video_link = f"https://example.com/videos/{prompt.replace(' ', '_')}.mp4"

    return JSONResponse({
        "status": "success",
        "prompt": prompt,
        "video_url": video_link
    })

