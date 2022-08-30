from re import match

from aiogram import types
from loguru import logger

from config.messages import ORDER_INVALID_D_LOAD
from config.messages import ORDER_ENTER_I_LOAD
from config.messages import ORDER_INVALID_I_LOAD
from config.messages import ORDER_ENTER_TIME
from config.messages import ORDER_INVALID_TIME
from config.messages import ORDER_ENTER_LOGIN
from states import order_states
from loader import user_settings
from loader import dp


'''
Ввод нагрузка на процессор 
при обычном использовании пк 
'''
@logger.catch
@dp.message_handler(content_types='text', state=order_states.choose_deafult_load_on_CPU)
async def _(message: types.Message):
    user_id = message.from_id

    logger.info(f'{user_id} type load cpu')

    if not message.text.isdigit():
        logger.error(f'{user_id} invalid load')

        await message.answer(ORDER_INVALID_D_LOAD)
        await dp.bot.delete_message(user_id, message.message_id-1)
        await dp.bot.delete_message(user_id, message.message_id)

        return

    load_cpu = int(message.text)
    if load_cpu < 0 or load_cpu > 100:
        logger.error(f'{user_id} invalid load')

        await message.answer(ORDER_INVALID_D_LOAD)
        await dp.bot.delete_message(user_id, message.message_id-1)
        await dp.bot.delete_message(user_id, message.message_id)

        return

    user_settings[user_id]['default_load_on_cpu'] = load_cpu
    await dp.current_state(user=user_id).set_state(order_states.choose_inaction_load_on_CPU)
    await message.answer(ORDER_ENTER_I_LOAD)

    logger.success(f'{user_id} load is valid')


'''
Ввод нагрузки на процессор
при длительном бездействии
'''
@logger.catch
@dp.message_handler(content_types='text', state=order_states.choose_inaction_load_on_CPU)
async def _(message: types.Message):
    user_id = message.from_id

    logger.info(f'{user_id} type load cpu(inactive)')

    if not message.text.isdigit():
        await message.answer(ORDER_INVALID_I_LOAD)
        logger.error(f'{user_id} invalid load(inactive)')
        return

    load_cpu = int(message.text)
    if load_cpu < 0 or load_cpu > 100:
        await message.answer(ORDER_INVALID_I_LOAD)
        logger.error(f'{user_id} invalid load(inactive)')
        return

    user_settings[user_id]['inaction_load_on_cpu'] = load_cpu
    await dp.current_state(user=user_id).set_state(order_states.inaction_time)
    await message.answer(ORDER_ENTER_TIME)

    logger.success(f'{user_id} load is valid(inactive)')


'''
Ввод времени бездействия
при котором нагрузка меняется 
720 - 12 часов 
взято из головы
5 тоже  
'''


@logger.catch
@dp.message_handler(content_types='text', state=order_states.inaction_time)
async def _(message: types.Message):
    user_id = message.from_id

    logger.info(f'{user_id} type inaction time')

    if not message.text.isdigit():
        logger.error(f'{user_id} invalid time')

        await message.answer('Введите число(минут)')
        await dp.bot.delete_message(user_id, message.message_id-1)
        await dp.bot.delete_message(user_id, message.message_id)

        return

    inaction_time = int(message.text)
    min_time, max_time = 5, 720
    if inaction_time < min_time or inaction_time > max_time:
        logger.error(f'{user_id} invalid time')

        await message.answer(ORDER_INVALID_TIME % (min_time, max_time))
        await dp.bot.delete_message(user_id, message.message_id-1)
        await dp.bot.delete_message(user_id, message.message_id)

        return

    user_settings[user_id]['inaction_time'] = inaction_time

    await dp.current_state(user=user_id).set_state(order_states.enter_login)
    await message.answer(ORDER_ENTER_LOGIN)

    logger.success(f'{user_id} inaction time valid')
