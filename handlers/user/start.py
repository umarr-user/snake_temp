from loader import dp, bot, types


@dp.message_handler(commands=['start'])
async def on_start(get: types.Message, ):
    text = 'Привет, пользователь'
    await get.answer(text=text)
