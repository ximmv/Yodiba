from aiogram import Router, F
from aiogram.types import Message

from bot.keyboards.image import image_styles

router = Router()


@router.message(F.text == "💬 Yangi suhbat")
async def new_chat(message: Message):
    await message.answer(
        "💬 Yangi suhbat boshlandi.\n\n"
        "Menga istalgan savolingizni yozing."
    )


@router.message(F.text == "🖼️ Rasm yaratish")
async def image(message: Message):
    await message.answer(
        "🖼️ <b>Rasm yaratish funksiyasiga xush kelibsiz!</b>\n\n"
        "🎨 Iltimos, rasm uslubini tanlang.\n\n"
        "Shundan so'ng yaratmoqchi bo'lgan rasmingizni tavsiflab yozing.",
        reply_markup=image_styles,
    )


@router.message(F.text == "🎬 Video yaratish")
async def video(message: Message):
    await message.answer(
        "🎬 Video yaratish funksiyasi tez orada qo'shiladi."
    )


@router.message(F.text == "🎵 Musiqa yaratish")
async def music(message: Message):
    await message.answer(
        "🎵 Musiqa yaratish funksiyasi tez orada qo'shiladi."
    )


@router.message(F.text == "🧠 AI vositalari")
async def ai_tools(message: Message):
    await message.answer(
        "🧠 AI vositalari bo'limi ishlab chiqilmoqda."
    )


@router.message(F.text == "👤 Profil")
async def profile(message: Message):
    user = message.from_user

    await message.answer(
        f"👤 Profil\n\n"
        f"🆔 ID: <code>{user.id}</code>\n"
        f"👤 Ism: {user.first_name}"
    )


@router.message(F.text == "⭐ Premium")
async def premium(message: Message):
    await message.answer(
        "⭐ Premium funksiyasi tez orada qo'shiladi."
    )


@router.message(F.text == "⚙️ Sozlamalar")
async def settings(message: Message):
    await message.answer(
        "⚙️ Sozlamalar bo'limi ishlab chiqilmoqda."
    )


@router.message(F.text == "📢 Yangiliklar")
async def news(message: Message):
    await message.answer(
        "📢 Hozircha yangiliklar mavjud emas."
    )


@router.message(F.text == "ℹ️ Yordam")
async def help_handler(message: Message):
    await message.answer(
        "ℹ️ Savolingiz bo'lsa, shu bot orqali yozishingiz mumkin."
    )