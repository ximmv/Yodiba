import asyncio

from aiogram import Dispatcher

from config.config import bot
from bot.handlers.start import router as start_router


async def main():
    dp = Dispatcher()

    dp.include_router(start_router)

    print("✅ Bot ishga tushdi!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
from bot.handlers.start import router as start_router
from bot.handlers.menu import router as menu_router
dp.include_router(start_router)
dp.include_router(menu_router)