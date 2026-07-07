import base64
from io import BytesIO

from bot.ai.client import client


async def generate_image(prompt: str):
    try:

        interaction = client.interactions.create(
            model="gemini-3.1-flash-image",
            input=prompt,
        )

        image_bytes = base64.b64decode(
            interaction.output_image.data
        )

        return BytesIO(image_bytes)

    except Exception as e:
        return str(e)