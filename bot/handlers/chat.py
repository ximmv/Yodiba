from aiogram import Router
from aiogram.enums import ChatAction
from aiogram.types import Message

from bot.ai.gemini import generate_text

router = Router()