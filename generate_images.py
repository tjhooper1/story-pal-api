import os
import requests
import openai

# Initialize OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_images(story_text):
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
