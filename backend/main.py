from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>🚀 VeoAI-Pro is running successfully!</h1><p>This is a test FastAPI app.</p>"
