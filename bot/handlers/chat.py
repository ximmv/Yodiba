await message.bot.send_chat_action(
    chat_id=message.chat.id,
    action=ChatAction.TYPING,
)

response = await generate_text(text)

await message.answer(response)