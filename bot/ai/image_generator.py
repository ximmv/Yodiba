import asyncio
from io import BytesIO

from google import genai
from google.genai import types

from config.settings import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

IMAGE_MODEL = "gemini-2.5-flash-image"


def _generate_image_sync(prompt: str) -> BytesIO | None:
    response = client.models.generate_content(
        model=IMAGE_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
        ),
    )

    for part in response.parts:
        if part.inline_data is not None:
            return BytesIO(part.inline_data.data)

    return None


async def generate_image(prompt: str) -> BytesIO | None:
    """
    Gemini (Nano Banana) orqali rasm yaratadi.
    Muvaffaqiyatli bo'lsa BytesIO obyekt, aks holda None qaytaradi.
    """
    try:
        return await asyncio.to_thread(_generate_image_sync, prompt)
    except Exception as e:
        print(f"[image_generator] Xatolik: {e}")
        return None