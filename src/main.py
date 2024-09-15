from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn
from .story_generator import generate_story


app = FastAPI()

class StoryRequest(BaseModel):
    prompt: str

@app.post('/generate-story')
async def generate_story(request: StoryRequest):
    try:
        video_path = generate_story(request.prompt)
        # Clean up temporary files if needed
        return FileResponse(video_path, media_type='video/mp4', filename='story.mp4')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
