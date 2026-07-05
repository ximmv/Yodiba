from google import genai

from config.settings import GEMINI_API_KEY
from database import get_history, save_message

client = genai.Client(api_key=GEMINI_API_KEY)


async def generate_text(user_id: int, prompt: str) -> str:
    try:
        history = get_history(user_id)

        contents = []

        for msg in history:
            contents.append(
                f"{msg['role']}: {msg['text']}"
            )

        contents.append(f"user: {prompt}")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="\n".join(contents),
        )

        answer = response.text or "❌ Javob olinmadi."

        save_message(user_id, "user", prompt)
        save_message(user_id, "assistant", answer)

        return answer

    except Exception as e:
        return f"❌ Xatolik:\n{e}"