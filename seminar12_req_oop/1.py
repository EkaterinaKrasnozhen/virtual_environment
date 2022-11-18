#mdn коды выполнения запроса
# pip install requests
#selenium.dev спец драйверы для браузеров, тестирует сайт как пользователь
# nic.ru кто есть кто по сайтам, доменам


# ctrl+d  = копия строки

import xml.etree.ElementTree as ET
import requests
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
# r = requests.get(url)
# print(r.status_code)
# if r.status_code == 200: #if r.ok is True или r.ok:  и так True передает
#     print(r.headers)
#     print(r.cookies)
#     print(r.text)
#     print(r.content)
#     print(r.ok)
    
responce = requests.get(url)
new_session = requests.Session()
responce = new_session.get(url)
if responce.status_code == 200: #if r.ok is True или r.ok:  и так True передает
    crb_xml = responce.text
    print(crb_xml)
    cur_root = 