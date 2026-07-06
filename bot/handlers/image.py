from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == "style_realistic")
async def realistic(callback: CallbackQuery):
    await callback.message.edit_text(
        "🎨 <b>Realistik uslub tanlandi.</b>\n\n"
        "Endi qanday rasm yaratmoqchi ekanligingizni yozing.\n\n"
        "Masalan:\n"
        "<i>Qorli tog' ustida turgan oq bo'ri</i>"
    )
    await callback.answer()


@router.callback_query(F.data == "style_anime")
async def anime(callback: CallbackQuery):
    await callback.message.edit_text(
        "🎭 <b>Anime uslubi tanlandi.</b>\n\n"
        "Endi rasm tavsifini yozing."
    )
    await callback.answer()


@router.callback_query(F.data == "style_3d")
async def style3d(callback: CallbackQuery):
    await callback.message.edit_text(
        "🌌 <b>3D uslubi tanlandi.</b>\n\n"
        "Endi rasm tavsifini yozing."
    )
    await callback.answer()


@router.callback_query(F.data == "style_photo")
async def photo(callback: CallbackQuery):
    await callback.message.edit_text(
        "📸 <b>Foto uslubi tanlandi.</b>\n\n"
        "Endi rasm tavsifini yozing."
    )
    await callback.answer()


@router.callback_query(F.data == "style_pixar")
async def pixar(callback: CallbackQuery):
    await callback.message.edit_text(
        "🧒 <b>Pixar uslubi tanlandi.</b>\n\n"
        "Endi rasm tavsifini yozing."
    )
    await callback.answer()


@router.callback_query(F.data == "style_digital")
async def digital(callback: CallbackQuery):
    await callback.message.edit_text(
        "🖌️ <b>Digital Art uslubi tanlandi.</b>\n\n"
        "Endi rasm tavsifini yozing."
    )
    await callback.answer()