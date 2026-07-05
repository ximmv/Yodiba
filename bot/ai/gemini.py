from google import genai

from config.settings import GEMINI_API_KEY
from database import get_history, save_message

client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """
Siz Yodiba nomli sun'iy intellekt yordamchisiz.

Qoidalar:
- Har doim muloyim va professional bo'ling.
- Foydalanuvchi qaysi tilda yozsa, o'sha tilda javob bering.
- Agar foydalanuvchi kod so'rasa, toza va ishlaydigan kod yozing.
- Agar biror narsani aniq bilmasangiz, taxmin qilib javob bermang, buni ochiq ayting.
- Javoblarni tushunarli va tartibli yozing.
- Keraksiz uzun javob bermang, lekin foydali ma'lumotni to'liq bering.
"""

async def generate_text(user_id: int, prompt: str) -> str:
    try:
        history = get_history(user_id)

        contents = [
            {
                "role": "user",
                "parts": [{"text": SYSTEM_PROMPT}]
            }
        ]

        for msg in history:
            contents.append(
                {
                    "role": msg["role"],
                    "parts": [{"text": msg["text"]}]
                }
            )

        contents.append(
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents,
        )

        answer = response.text or "❌ Javob olinmadi."

        save_message(user_id, "user", prompt)
        save_message(user_id, "model", answer)

        return answer

    except Exception as e:
        return f"❌ Xatolik:\n{e}"