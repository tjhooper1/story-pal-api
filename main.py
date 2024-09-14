from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn

from create_video import create_video
from generate_images import generate_images
from generate_narration_audio import generate_narration_audio
from generate_story_text import generate_story_text


app = FastAPI()

class StoryRequest(BaseModel):
    prompt: str

@app.post('/generate-story')
async def generate_story(request: StoryRequest):
    try:
        prompt = request.prompt
        story_text = generate_story_text(prompt)
        image_paths = generate_images(story_text)
        audio_path = generate_narration_audio(story_text)
        video_path = create_video(image_paths, audio_path)
        # Clean up temporary files if needed
        return FileResponse(video_path, media_type='video/mp4', filename='story.mp4')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
