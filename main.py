import os

from google.genai import types
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("A variável GEMINI_API_KEY não foi configurada.")

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=15000),
)
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Responda apenas: OK",
    config=types.GenerateContentConfig(
        max_output_tokens=20,
    ),
)

print(response.text)

print(response.text)
