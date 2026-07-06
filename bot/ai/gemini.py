from google import genai

from config.settings import GEMINI_API_KEY
from database import get_history, save_message

client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """
Siz Yodiba nomli sun'iy intellekt yordamchisiz.

QOIDALAR:

1. Foydalanuvchi qaysi tilda yozsa, o'sha tilda javob bering.

2. Javoblaringiz aniq, foydali va tushunarli bo'lsin.

3. Agar biror ma'lumotga ishonchingiz komil bo'lmasa, taxmin qilmang.
Buning o'rniga buni ochiq ayting.

4. Kod yozishda professional darajada ishlang.

5. Keraksiz uzun javob bermang.
Lekin foydalanuvchi batafsil tushuntirish so'rasa, to'liq javob bering.

6. O'zingizni OpenAI yoki Google deb tanishtirmang.
Siz Yodiba AI yordamchisisiz.

7. Foydalanuvchiga doimo hurmat bilan murojaat qiling.
"""


async def generate_text(user_id: int, prompt: str) -> str:
    try:
        history = get_history(user_id)

        conversation = SYSTEM_PROMPT + "\n\n"

        for msg in history:
            conversation += f"{msg['role']}: {msg['text']}\n"

        conversation += f"user: {prompt}"

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation,
        )

        answer = response.text or "Kechirasiz, javob olinmadi."

        save_message(user_id, "user", prompt)
        save_message(user_id, "assistant", answer)

        return answer

    except Exception as e:
        return f"❌ Xatolik:\n{e}"