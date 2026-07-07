from aiogram import Router
from aiogram.enums import ChatAction
from aiogram.types import Message, BufferedInputFile

from bot.ai.gemini import generate_text
from bot.ai.image_generator import generate_image
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

    # ==========================
    # IMAGE MODE
    # ==========================
    if message.from_user.id in image_sessions:

        style = image_sessions[message.from_user.id]

        await message.answer(
            "🎨 Uslub qabul qilindi.\n"
            f"📌 {style}\n\n"
            "⏳ Rasm yaratilmoqda..."
        )

        prompt = f"{style}\n\n{text}"

        image = await generate_image(prompt)

        del image_sessions[message.from_user.id]

        if image:

            await message.answer_photo(
                BufferedInputFile(
                    image.getvalue(),
                    filename="yodiba.png"
                ),
                caption="✅ Rasm tayyor!"
            )

        else:

            await message.answer(
                "❌ Rasm yaratishda xatolik yuz berdi."
            )

        return

    # ==========================
    # GEMINI CHAT
    # ==========================
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING,
    )

    response = await generate_text(
        user_id=message.from_user.id,
        prompt=text,
    )

    await message.answer(response)