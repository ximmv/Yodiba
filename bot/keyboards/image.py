from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

image_styles = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🎨 Realistik",
                callback_data="style_realistic",
            ),
            InlineKeyboardButton(
                text="🎭 Anime",
                callback_data="style_anime",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌌 3D",
                callback_data="style_3d",
            ),
            InlineKeyboardButton(
                text="📸 Foto",
                callback_data="style_photo",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🧒 Pixar",
                callback_data="style_pixar",
            ),
            InlineKeyboardButton(
                text="🖌️ Digital Art",
                callback_data="style_digital",
            ),
        ],
    ]
)