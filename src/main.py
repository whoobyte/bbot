import os

from aiogram import executor
from loguru import logger

from handlers import dp


async def startup(dp):
    from utils import set_default_commands
    await set_default_commands(dp)


async def shutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    logger.info(f'start')

    # папка с настройками майнеров 
    if not os.path.exists('./data/settings'):
        os.mkdir('./data/settings')

    executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown)