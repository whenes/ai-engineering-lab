from google import genai
from google.genai import types

from config import GEMINI_API_KEY

class LLMService:
    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY,
            http_options=types.HttpOptions(timeout=60000),
        )


    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
            config=types.GenerateContentConfig(
                max_output_tokens=300,
            ),
        )

        return response.text or ""

