from google import genai

from config.settings import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


async def generate_text(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        if response.text:
            return response.text

        return "❌ Javob olinmadi."

    except Exception as e:
        return f"❌ Xatolik:\n{e}"