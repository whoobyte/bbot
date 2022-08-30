from json import dump

from loguru import logger


'''
Ф-ция для записи настроек в файл
для последующей отправки   
'''
@logger.catch
def create_json(obj) -> bool:
    id = obj['id']
    with open(f'./data/settings/{id}.json', 'w+') as file:
        dump(obj, file)
        return True
    return False 