from aiogram import Dispatcher
from aiogram.types import BotCommand

bot_commands = [['start', 'Запуск бота'], ['help', 'Помощь']]


async def set_bot_commands(dp: Dispatcher):
    commands = list()
    for command in bot_commands:
        commands.append(BotCommand(command[0], command[1]))
    await dp.bot.set_my_commands(commands)
