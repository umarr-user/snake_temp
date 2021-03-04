from loader import dp, bot, db, types
from data import ADMINS


@dp.message_handler(commands=['start'], user_id=ADMINS)
async def on_start(get: types.Message,):
    text = 'Привет, Админ :)'
    await get.answer(text=text)
    id = await db.get(f'SELECT id FROM users WHERE id = {get.from_user.id}')
    text = str(id)
    await get.answer(text=text)
