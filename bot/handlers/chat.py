from aiogram import Router
from aiogram.enums import ChatAction
from aiogram.types import Message

from bot.ai.gemini import generate_text

router = Router()

@router.message()
async def chat_handler(message: Message):
text = message.text

if not text:
    return

await message.bot.send_chat_action(
    chat_id=message.chat.id,
    action=ChatAction.TYPING,
)

response = await generate_text(text)

await message.answer(response)