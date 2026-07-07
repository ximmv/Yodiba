import base64
from io import BytesIO

from bot.ai.client import client


async def generate_image(prompt: str):
    try:
        interaction = client.interactions.create(
            model="gemini-3.1-flash-image",
            input=prompt,
        )

        if not interaction.output_image:
            return None

        image_bytes = base64.b64decode(
            interaction.output_image.data
        )

        image = BytesIO(image_bytes)
        image.name = "image.png"

        return image

    except Exception as e:
        print(f"IMAGE ERROR: {e}")
        return None