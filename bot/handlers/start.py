from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.main_menu import main_menu

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    name = message.from_user.first_name

    await message.answer(
        f"👋 Assalomu alaykum, <b>{name}</b>!\n\n"

        "✨ <b>Yodiba AI</b> ga xush kelibsiz!\n\n"

        "🤖 Men sizning zamonaviy sun'iy intellekt yordamchingizman.\n\n"

        "📌 Quyidagi imkoniyatlardan foydalanishingiz mumkin:\n\n"

        "💬 <b>Yangi suhbat</b> — AI bilan erkin muloqot qiling.\n"
        "🖼️ <b>Rasm yaratish</b> — matndan professional rasmlar yarating.\n"
        "🎬 <b>Video yaratish</b> — AI yordamida videolar yarating.\n"
        "🎵 <b>Musiqa yaratish</b> — AI yordamida musiqa va audio yarating.\n"
        "🧠 <b>AI vositalari</b> — maxsus sun'iy intellekt funksiyalaridan foydalaning.\n"
        "👤 <b>Profil</b> — hisobingiz va foydalanish statistikangizni ko'ring.\n"
        "⭐ <b>Premium</b> — qo'shimcha imkoniyatlarni faollashtiring.\n"
        "⚙️ <b>Sozlamalar</b> — botni o'zingizga moslang.\n"
        "📢 <b>Yangiliklar</b> — yangi imkoniyatlardan xabardor bo'ling.\n"
        "ℹ️ <b>Yordam</b> — qo'llanma va bog'lanish ma'lumotlari.\n\n"

        "👇 Pastdagi menyudan kerakli bo'limni tanlang yoki menga istalgan savolingizni yuboring.\n\n"

        "<blockquote>🚀 Yodiba — aqlliroq ishlashning yangi usuli.</blockquote>",
        reply_markup=main_menu
    )