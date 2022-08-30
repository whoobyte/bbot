from loguru import logger
from aiogram import types

from config.messages import ORDER_INVALID_LOGIN
from config.messages import ORDER_ENTER_PASSWORD
from config.messages import ORDER_INVALID_PASSWORD
from config.messages import ORDER_SUCCESS
from utils import create_json
from utils import send_to_admin
from states import order_states
from loader import user_settings
from loader import dp


'''
enter login
'''
@logger.catch
@dp.message_handler(content_types='text', state=order_states.enter_login)
async def _(message: types.Message):
    user_id = message.from_id

    logger.info(f'{user_id} type login')

    login = message.text
    if len(login) > 20 or len(login) < 4:
        logger.error(f'{user_id} invalid login')

        await message.answer(ORDER_INVALID_LOGIN)
        await dp.bot.delete_message(user_id, message.message_id-1)
        await dp.bot.delete_message(user_id, message.message_id)

        return

    # проверка на существование такого логина
    if False:
        # логин должен записываться в бд

        return

    user_settings[user_id]['login'] = login
    await dp.current_state(user=user_id).set_state(order_states.enter_password)
    await message.answer(ORDER_ENTER_PASSWORD)

    logger.success(f'{user_id} login is valid')


'''
enter password
'''
@logger.catch
@dp.message_handler(content_types='text', state=order_states.enter_password)
async def _(message: types.Message):
    user_id = message.from_id

    logger.info(f'{user_id} type password')

    password = message.text

    if len(password) > 30 or len(password) < 4:
        logger.error(f'{user_id} invalid password')

        await message.answer(ORDER_INVALID_PASSWORD)
        await dp.bot.delete_message(user_id, message.message_id-1)
        await dp.bot.delete_message(user_id, message.message_id)

        return

    await dp.current_state(user=user_id).reset_state()

    logger.success(f'{user_id} password is valid')

    user_settings[user_id]['password'] = password
    user_settings[user_id] = {'id': user_id,
                              'settings': user_settings[user_id]}

    if not create_json(user_settings[user_id]):
        logger.error(f'{user_id} file wasnt created')
        return

    logger.success(f'{user_id} create settings file')

    del user_settings[user_id]
    logger.debug(f'user settings len {len(user_settings)}')

    await message.answer(ORDER_SUCCESS)

    if not await send_to_admin(user_id):
        await message.answer('Файл не был отправлен')
