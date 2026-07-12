import asyncio
import urllib.parse
from io import BytesIO

import requests

IMAGE_BASE_URL = "https://gen.pollinations.ai/image/"


def _generate_image_sync(prompt: str) -> BytesIO | None:
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"{IMAGE_BASE_URL}{encoded_prompt}"

    response = requests.get(url, timeout=60)

    if response.status_code != 200:
        raise Exception(f"HTTP {response.status_code}: {response.text[:200]}")

    return BytesIO(response.content)


async def generate_image(prompt: str) -> BytesIO | None:
    """
    Pollinations.ai orqali rasm yaratadi.
    Muvaffaqiyatli bo'lsa BytesIO obyekt, aks holda None qaytaradi.
    """
    try:
        return await asyncio.to_thread(_generate_image_sync, prompt)
    except Exception as e:
        print(f"[image_generator] Xatolik: {e}")
        return None