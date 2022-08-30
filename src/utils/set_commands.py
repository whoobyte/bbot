from aiogram import Dispatcher
from aiogram import types
from loguru import logger 


@logger.catch
async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand('help', 'справка'),
        types.BotCommand('about', 'о боте'),
        types.BotCommand('order', 'сделать заявку'),
        types.BotCommand('problem', 'возникла проблема?')
        ]
    )