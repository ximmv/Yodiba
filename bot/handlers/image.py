from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.image_sessions import image_sessions

router = Router()


@router.callback_query(F.data == "style_realistic")
async def realistic(callback: CallbackQuery):
    image_sessions[callback.from_user.id] = "🎨 Realistik"

    await callback.message.edit_text(
        "🎨 <b>Realistik uslub tanlandi.</b>\n\n"
        "📝 Endi yaratmoqchi bo'lgan rasmingizni batafsil yozing.\n\n"
        "Masalan:\n"
        "<i>Qorli tog' ustida turgan oq bo'ri, ultra realistik, 8K.</i>"
    )

    await callback.answer()


@router.callback_query(F.data == "style_anime")
async def anime(callback: CallbackQuery):
    image_sessions[callback.from_user.id] = "🎭 Anime"

    await callback.message.edit_text(
        "🎭 <b>Anime uslubi tanlandi.</b>\n\n"
        "📝 Endi yaratmoqchi bo'lgan rasmingizni yozing."
    )

    await callback.answer()


@router.callback_query(F.data == "style_3d")
async def style3d(callback: CallbackQuery):
    image_sessions[callback.from_user.id] = "🌌 3D"

    await callback.message.edit_text(
        "🌌 <b>3D uslubi tanlandi.</b>\n\n"
        "📝 Endi yaratmoqchi bo'lgan rasmingizni yozing."
    )

    await callback.answer()


@router.callback_query(F.data == "style_photo")
async def photo(callback: CallbackQuery):
    image_sessions[callback.from_user.id] = "📸 Foto"

    await callback.message.edit_text(
        "📸 <b>Foto uslubi tanlandi.</b>\n\n"
        "📝 Endi yaratmoqchi bo'lgan rasmingizni yozing."
    )

    await callback.answer()


@router.callback_query(F.data == "style_pixar")
async def pixar(callback: CallbackQuery):
    image_sessions[callback.from_user.id] = "🧒 Pixar"

    await callback.message.edit_text(
        "🧒 <b>Pixar uslubi tanlandi.</b>\n\n"
        "📝 Endi yaratmoqchi bo'lgan rasmingizni yozing."
    )

    await callback.answer()


@router.callback_query(F.data == "style_digital")
async def digital(callback: CallbackQuery):
    image_sessions[callback.from_user.id] = "🖌️ Digital Art"

    await callback.message.edit_text(
        "🖌️ <b>Digital Art uslubi tanlandi.</b>\n\n"
        "📝 Endi yaratmoqchi bo'lgan rasmingizni yozing."
    )

    await callback.answer()