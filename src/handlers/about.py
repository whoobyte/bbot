from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import text
from aiogram.utils.markdown import bold 
from aiogram import types
from loguru import logger

from config.messages import ABOUT_MESSAGE
from loader import dp


@logger.catch 
@dp.message_handler(commands='about')
async def _(message: types.Message):
    logger.info(f'{message.from_id} about')
    await message.answer(ABOUT_MESSAGE)