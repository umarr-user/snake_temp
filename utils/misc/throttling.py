from asyncio import sleep
from loader import bot, types


async def on_throttled(*args, **kwargs):
    get: types.Message = args[0]
    text = 'Не спамьте'
    msg = await get.answer(text=text)
    await sleep(2)
    await get.delete()
    await bot.delete_message(chat_id=get.from_user.id, message_id=msg.message_id)
