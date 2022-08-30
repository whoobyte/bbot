from aiogram import types
from loguru import logger

from states import order_states
from config.messages import ORDER_CANCEL
from loader import user_settings
from loader import dp


'''
Удаление уже введенных данных 
'''
@logger.catch
@dp.callback_query_handler(lambda call: call.data == 'yes', state=order_states.all_states)
async def _(call: types.CallbackQuery):
    user_id = call.from_user.id

    await dp.bot.delete_message(user_id, call.message.message_id-1)
    await dp.bot.delete_message(user_id, call.message.message_id)
    await dp.current_state(user=user_id).reset_state()
    await dp.bot.send_message(user_id, ORDER_CANCEL)

    logger.debug(f'{user_id} reset state')

    del user_settings[user_id]
    logger.debug(f'user_settings len: {len(user_settings)}')


'''
Отмена собственно 
Состояние не сбрасывается 
'''
@logger.catch
@dp.callback_query_handler(lambda call: call.data == 'no', state=order_states.all_states)
async def _(call: types.CallbackQuery):
    user_id = call.from_user.id

    await dp.bot.delete_message(user_id, call.message.message_id-1)
    await dp.bot.delete_message(user_id, call.message.message_id)

    logger.debug(f'{user_id} cancel reset state')
