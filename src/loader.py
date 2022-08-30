from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

from config import TOKEN


bot: Bot = Bot(token=TOKEN, parse_mode=None)
dp: Dispatcher = Dispatcher(bot, storage = MemoryStorage())


user_settings = {}    # настройки сборки пользователей 
user_recipient = [None] # id пользователя, которому отправляется сборка 
                        # list тк обычная переменная не изменяется в разных файлах одинаково 
                        # или что-то такое 