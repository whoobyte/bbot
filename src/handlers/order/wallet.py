from re import match

from aiogram import types
from loguru import logger

from config.messages import ORDER_INVALID_WALLET
from config.messages import ORDER_ENTER_D_LOAD
from states import order_states
from loader import user_settings
from loader import dp


'''
Ввод адреса кошелька
'''
@logger.catch
@dp.message_handler(content_types='text', state=order_states.enter_wallet)
async def _(message: types.Message):
    user_id = message.from_id
    logger.info(f'{user_id} type wallet')

    if not match(r'^[\d | \w]{95}$', message.text):
        logger.error(f'{user_id} invalid wallet')

        await message.answer(ORDER_INVALID_WALLET)
        await dp.bot.delete_message(message.from_id, message.message_id-1)
        await dp.bot.delete_message(message.from_id, message.message_id)

        return

    await dp.current_state(user=user_id).set_state(order_states.choose_deafult_load_on_CPU)
    await message.answer(ORDER_ENTER_D_LOAD)
    user_settings[user_id]['wallet'] = message.text

    logger.success(f'{user_id} wallet is valid')
