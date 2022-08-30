from aiogram import types
from loguru import logger

from config.messages import ORDER_CANCEL_WARNING
from config.messages import ORDER_ENTER_WALLET
from states import order_states
from loader import user_settings
from loader import dp


'''
Если уже собирались какие-то данные 
'''
@logger.catch
@dp.message_handler(commands='order', state=order_states.all_states)
async def _(message: types.Message):
    logger.info(f'{message.from_id} order(with state)')

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Да', callback_data='yes'))
    markup.add(types.InlineKeyboardButton(text='Нет', callback_data='no'))

    await message.answer(ORDER_CANCEL_WARNING, reply_markup=markup)


'''
Начало сбора данных о заказе
(кошелёк, мощность и тд и тп)
'''
@logger.catch
@dp.message_handler(commands='order', state='*')
async def _(message: types.Message):
    logger.info(f'{message.from_id} order')

    user_id = message.from_id

    await dp.current_state(user=user_id).set_state(order_states.enter_wallet)

    await message.answer(ORDER_ENTER_WALLET)

    user_settings[user_id] = {}
    logger.debug(f'user_settings len: {len(user_settings)}')
