from os import getenv

from dotenv import load_dotenv


load_dotenv()


TOKEN = getenv('BOT_TOKEN')
DB_PATH = getenv('DB_PATH')
ADMINS_ID = getenv('ADMINS_ID')


if TOKEN is None:
    raise SystemExit('TG Token is not defined')

if ADMINS_ID is None:
    raise SystemExit('Admins id is not defined')
