import google.generativeai as genai

from config.settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


async def generate_text(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)

        if response.text:
            return response.text

        return "❌ Javob olinmadi."

    except Exception as e:
        return f"❌ Xatolik:\n{e}"