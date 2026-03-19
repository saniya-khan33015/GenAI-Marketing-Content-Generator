import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenRouter API key from environment
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if OPENROUTER_API_KEY:
    OPENROUTER_API_KEY = OPENROUTER_API_KEY.strip()

def generate_content(prompt):
    """
    Generate content using OpenRouter (ChatGPT API).
    Returns only the generated message content.
    Handles errors gracefully.
    """
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "GenAI Project"
    }
    data = {
        "model": "openai/gpt-4o",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"API request error: {e}"
    except (KeyError, IndexError) as e:
        return f"Unexpected API response format: {e}"
    except Exception as e:
        return f"Error generating content: {e}"
