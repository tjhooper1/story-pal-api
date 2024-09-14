import os
import openai

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
    
    