from datetime import datetime

from aiogram.utils.markdown import text
from aiogram.utils.markdown import bold
from aiogram import types
from loguru import logger

from states import problem_states
from config.messages import PROBLEM_DESCRIPTION
from config.messages import PROBLEM_CANCEL
from config.messages import PROBLEM_SEND_SUCCESS
from config import ADMINS_ID
from loader import dp


''' 
Отмена жалобы
'''
@logger.catch
@dp.message_handler(commands='problem', state=problem_states.all_states)
async def _(message: types.Message):
    user_id = message.from_id
    
    logger.info(f'{user_id} problem cancel')

    await message.answer(PROBLEM_CANCEL)
    
    await dp.current_state(user=user_id).reset_state()
    
    
''' 
Жалоба/Проблема 
'''
@logger.catch
@dp.message_handler(commands='problem', state='*')
async def _(message: types.Message):
    user_id = message.from_id
    
    logger.info(f'{user_id} problem')

    await message.answer(PROBLEM_DESCRIPTION)
    
    await dp.current_state(user=user_id).set_state(problem_states.describes_problem)
    

''' 
Описание проблемы и отправка его админу 
'''
@logger.catch
@dp.message_handler(content_types='text', state=problem_states.describes_problem)
async def _(message: types.Message):
    user_id = message.from_id
    user_name = message.from_user.first_name
    
    logger.info(f'{user_id} sent a complaint')
    
    asnwer = text(
        f'Жалоба от пользователя: {bold(user_id)} {bold(user_name)}', '',
        message.text, '',
        datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        sep='\n'
    )
    
    await dp.current_state(user=user_id).reset_state()
    await dp.bot.send_message(chat_id=ADMINS_ID, text=asnwer, parse_mode=types.ParseMode.MARKDOWN)
    await message.answer(PROBLEM_SEND_SUCCESS)
    
    logger.success(f'admin got complaint ')