from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "✨ <b>Yodiba AI</b> ga xush kelibsiz!\n\n"
        "Sizning zamonaviy sun'iy intellekt yordamchingiz.\n\n"
        "📌 Men sizga quyidagi yo'nalishlarda yordam bera olaman:\n\n"
        "💬 Savollarga javob berish\n"
        "📝 Matn yozish va tahrirlash\n"
        "🌍 Tarjima qilish\n"
        "💻 Dasturlash va kod yozish\n"
        "📚 Ta'lim va tushuntirishlar\n"
        "💡 G'oyalar va tavsiyalar berish\n"
        "🖼️ Rasmlar bilan ishlash\n\n"
        "🚀 Boshlash uchun istalgan xabar yoki savolingizni yuboring.\n\n"
        "<i>Yodiba — aqlliroq ishlashning yangi usuli.</i>"
    )
