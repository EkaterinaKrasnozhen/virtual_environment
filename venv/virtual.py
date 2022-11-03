# создать виртуальное окружение"
# python -m venv venv (или последнее любое название)
# venv\Scripts\activate.bat

# deactivate деактивировать

# pip freeze > requirements.txt создать файл со списком библиотек
# cat requirements.txt - просмотр (не работал)
# pip install -r requirements.txt
# pip list посмотреть библиотеки
# pypi.org сайт с библотеками еще pandas, numpy
# nano requirements.txt работа с библиотеками, записать, удалить и тд
# set посмотреть переменное окружение

# д/з python tictactoe из pypi.org для крестиков ноликов
import os
from dotenv import load_dotenv # pip install python-dotenv - безопасно ипсользовать свои пароли и токены
load_dotenv()
token = os.getenv('token_tg')
my_path = os.getenv('PATH')
print(token)
print(my_path)