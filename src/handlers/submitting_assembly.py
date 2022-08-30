from aiogram import types
from loguru import logger

from config.messages import USER_NOT_SELECTED
from config.messages import SENT_ASSEMBLY_SUCCESS
from config import ADMINS_ID
from loader import user_recipient
from loader import dp


'''
Отправка exe файла пользователю
'''
@logger.catch
@dp.message_handler(content_types='document')
async def _(message: types.Message):
    user_id = str(message.from_id)
    
    if user_id != ADMINS_ID:
        logger.debug(f'{user_id} sent document')
        return
    
    if user_recipient[0] is None:
        logger.debug('user_recipient is None')      
        
        await message.answer(USER_NOT_SELECTED)
        
        return
    
    await message.send_copy(user_recipient[0])
    await message.answer(SENT_ASSEMBLY_SUCCESS)
    
    logger.success(f'Success {user_recipient[0]} got document')
    
    user_recipient[0] = None