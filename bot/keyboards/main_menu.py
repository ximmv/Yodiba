from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💬 Yangi suhbat"),
            KeyboardButton(text="🖼️ Rasm yaratish"),
        ],
        [
            KeyboardButton(text="🎬 Video yaratish"),
            KeyboardButton(text="🎵 Musiqa yaratish"),
        ],
        [
            KeyboardButton(text="🧠 AI vositalari"),
            KeyboardButton(text="👤 Profil"),
        ],
        [
            KeyboardButton(text="⭐ Premium"),
            KeyboardButton(text="⚙️ Sozlamalar"),
        ],
        [
            KeyboardButton(text="📢 Yangiliklar"),
            KeyboardButton(text="ℹ️ Yordam"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Savolingizni yozing..."
)