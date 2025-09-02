from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "🎬 Video Factory API running on Render!"}

@app.post("/generate-video")
async def generate_video():
    # 这里先写个假返回，确保接口能通
    return {"status": "success", "video_url": "https://example.com/video.mp4"}
