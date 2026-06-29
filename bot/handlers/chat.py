from aiogram import Router
from aiogram.enums import ChatAction
from aiogram.types import Message

from bot.ai.gemini import generate_text
from database import add_user

router = Router()


@router.message()
async def chat_handler(message: Message):
    text = message.text

    if not text:
        return

    # Foydalanuvchini bazaga qo'shish
    add_user(
        user_id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username,
    )

    # Telegram'da "typing..." animatsiyasini ko'rsatish
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING,
    )

    # Gemini'dan javob olish (tarix bilan)
    response = await generate_text(
        user_id=message.from_user.id,
        prompt=text,
    )

    await message.answer(response)