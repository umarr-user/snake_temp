from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.chat import ChatActions
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.models.db import Sqlite
from utils.models.set_commands import set_bot_commands
from data import TOKEN

bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Sqlite()


async def startup(dp: Dispatcher):
    await set_bot_commands(dp)


async def shutdown(dp: Dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()


def dp_import():
    from handlers import dp
    return dp


def launch(dp: Dispatcher):
    executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown)


if __name__ == '__main__':
    launch(dp_import())
