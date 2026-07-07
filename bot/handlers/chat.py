from aiogram import Router
from aiogram.enums import ChatAction
from aiogram.types import Message

from bot.ai.gemini import generate_text
from bot.image_sessions import image_sessions
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

    # ===============================
    # IMAGE MODE
    # ===============================
    if message.from_user.id in image_sessions:

        style = image_sessions[message.from_user.id]

        del image_sessions[message.from_user.id]

        await message.answer(
            f"🖼 <b>Rasm yaratish so'rovi qabul qilindi.</b>\n\n"
            f"🎨 Uslub: {style}\n"
            f"📝 Tavsif:\n"
            f"<blockquote>{text}</blockquote>\n\n"
            f"⏳ Hozircha bu test rejimi.\n"
            f"Keyingi bosqichda AI ushbu tavsif asosida rasm yaratadi."
        )

        return

    # ===============================
    # GEMINI CHAT
    # ===============================
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING,
    )

    response = await generate_text(
        user_id=message.from_user.id,
        prompt=text,
    )

    await message.answer(response)