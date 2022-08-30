from aiogram.dispatcher.filters.state import StatesGroup, State

'''
Состояния ввода данных для натсройки майнера 

enter_wallet                   - ввод кошелька
enter_login                    - ввод логина 
enter_password                 - ввод пароля 
choose_deafult_load_on_CPU     - нагрузка на процессор в обычном режиме раоты   
choose_inaction_load_on_CPU    - нагрузка на процессов в бездействии
incation_time                  - время бездействия 
'''
class order_states(StatesGroup):
    enter_wallet = State()
    enter_login = State()
    enter_password = State()
    choose_deafult_load_on_CPU = State()
    choose_inaction_load_on_CPU = State()
    inaction_time = State()
    

'''
Состояния при описании некой проблемы 
'''
class problem_states(StatesGroup):
    describes_problem = State()