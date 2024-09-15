import os
import openai
import requests
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

# Initialize OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_story_text(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates a story based on the given prompt."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise Exception(f"Error generating story text: {e}")

def generate_images(story_text) -> list[str]:
    try:
        segments = story_text.split('. ')
        image_paths = []
        for i, segment in enumerate(segments):
            if segment and i < 4:
                image_response = openai.images.generate(
                    model="dall-e-3",
                    prompt=segment.strip(),
                    n=1,
                    size="1024x1024",
                    quality="standard"
                )
                # The response structure has changed, so we need to access the URL differently
                image_url = image_response.data[0].url
                image_data = requests.get(image_url).content
                image_path = f"image_{i}.png"
                with open(image_path, "wb") as f:
                    f.write(image_data)
                image_paths.append(image_path)
        return image_paths
    except Exception as e:
        raise Exception(f"Error generating images: {e}")
    
def generate_narration_audio(story_text):
    try:
        # Placeholder for TTS implementation
        # Replace this with actual API calls to your chosen TTS service
        audio_path = 'narration.mp3'
        # For example, using gTTS (Google Text-to-Speech)
        from gtts import gTTS
        tts = gTTS(text=story_text, lang='en')
        tts.save(audio_path)
        return audio_path
    except Exception as e:
        raise Exception(f"Error generating narration audio: {e}")

def create_video(image_paths, audio_path):
    try:
        audio_clip = AudioFileClip(audio_path)
        duration_per_image = audio_clip.duration / len(image_paths)
        image_clips = []

        for image_path in image_paths:
            clip = ImageClip(image_path).set_duration(duration_per_image)
            image_clips.append(clip)

        video_clip = concatenate_videoclips(image_clips, method="compose")
        video_clip = video_clip.set_audio(audio_clip)
        output_path = 'story.mp4'
        video_clip.write_videofile(output_path, fps=24)
        return output_path
    except Exception as e:
        raise Exception(f"Error creating video: {e}")

def generate_story(prompt) -> str:
    story_text = generate_story_text(prompt)
    image_paths = generate_images(story_text)
    audio_path = generate_narration_audio(story_text)
    video_path = create_video(image_paths, audio_path)
    return video_path