from loader import dp, bot, types
from utils.misc.throttling import on_throttled


@dp.message_handler(commands=['start'])
@dp.throttled(on_throttled, rate=3)
async def on_start(get: types.Message, ):
    text = 'Привет, пользователь'
    await get.answer(text=text)
