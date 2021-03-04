from loader import dp, bot, types
from utils.misc.throttling import on_throttled
from data import ADMINS


@dp.message_handler(commands=['start'], user_id=ADMINS)
@dp.throttled(on_throttled, rate=3)
async def on_start(get: types.Message,):
    text = 'Привет, Админ :)'
    await get.answer(text=text)
