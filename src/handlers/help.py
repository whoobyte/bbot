from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import text
from aiogram.utils.markdown import bold 
from aiogram import types
from loguru import logger

from config.messages import HELP_COMMANDS
from config import ADMINS_ID
from loader import dp


@dp.message_handler(Command('help'), state='*')
async def _(message: types.Message):
    logger.info(f'{message.from_id} help')
    
    status_m = bold(
        f'Ваш статус: {"admin" if message.from_id == int(ADMINS_ID) else "user"}\n'
    )
    msg =  status_m + HELP_COMMANDS
        
    await message.answer(msg, parse_mode=types.ParseMode().MARKDOWN)
    