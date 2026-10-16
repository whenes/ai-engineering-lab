from google import genai
from google.genai import types

from config import GEMINI_API_KEY


class LLMService:
    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY,
            http_options=types.HttpOptions(timeout=60000),
        )

    def generate(self, history: list[dict[str, str]]) -> str:
        response = self.client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=[
                types.Content(
                    role=message["role"],
                    parts=[types.Part.from_text(text=message["content"])],
                )
                for message in history
            ],
            config=types.GenerateContentConfig(
                max_output_tokens=600,
            ),
        )

        return response.text or ""