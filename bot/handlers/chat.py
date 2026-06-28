from aiogram import Router
from aiogram.types import Message

from bot.ai.gemini import generate_text

router = Router()


@router.message()
async def chat_handler(message: Message):
    text = message.text

    if not text:
        return

    wait = await message.answer("✍️Yozmoqda...")

    response = await generate_text(text)

    await wait.edit_text(response)