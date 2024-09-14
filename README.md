# Story Pal API

## Description

This API generates a story, images, narration, and a video based on a given prompt.

## Installation

1. Clone the repository
2. Install the dependencies

```bash
pip install -r requirements.txt
```

```bash
uvicorn main:app --reload
```

## How To Use
1. Create a `.env` file with the following environment variables:
```bash
OPENAI_API_KEY=<your-openai-api-key>
```
2. Run the API
3. Visit `http://127.0.0.1:8000/docs` to see the API documentation

4. Send a POST request to the `/generate-story` endpoint with a JSON body containing the prompt

```bash
curl -X POST "http://127.0.0.1:8000/generate-story" -H "Content-Type: application/json" -d "{\"prompt\": \"A story about a cat\"}"

