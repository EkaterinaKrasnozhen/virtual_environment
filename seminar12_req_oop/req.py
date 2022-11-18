#mdn коды выполнения запроса
# pip install requests
#selenium.dev спец драйверы для браузеров, тестирует сайт как пользователь
# nic.ru кто есть кто по сайтам, доменам
# beautiful soup разбор xml/html страниц лучше с lxml


# ctrl+d  = копия строки

import xml.etree.ElementTree as ET
import requests
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
# на дату 'http://www.cbr.ru/scripts/XML_daily.asp?date_reg=14.12.2014'
params = {'date_reg' : '14.12.2014'}
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
responce = new_session.get(url) # .get(url, params=params)
if responce.status_code == 200: #if r.ok is True или r.ok:  и так True передает
    crb_xml = responce.text
    cur_root = ET.fromstring(crb_xml) # ET.parse('file.xml') по аналогии можно открыть в файл
    # print(cur_root.tag)
    # #print(cur_root.text)
    # print(cur_root.attrib)
    # print(cur_root.attrib['Date'])
    # #for i in cur_root:
    # #     print(i.tag)
    # #     print(i.text)
    # #     print(i.attrib)
        
    # print(cur_root[0].tag)
    
    # for i in cur_root.findall('Valute'):
    #     cur_name = i.find('Name').text
    #     cur_nom = i.find('Nominal').text
    #     cur_char = i.find('CharCode').text
    #     cur_val = i.find('Value').text
    #     print(cur_char,cur_name,cur_nom, cur_val) #все валюты
        
cny_find = cur_root.find("Valute[CharCode='CNY']")
print(cny_find.attrib)
yen_name = cny_find.findtext('Name')
yen_nom = cny_find.findtext('Nominal')
yen_char = cny_find.findtext('CharCode')
yen_val = cny_find.findtext('Value')
print(yen_name, yen_char, yen_nom, yen_val)
yen_nom = int(yen_nom)  # type: ignore
yen_val = yen_val.replace(',', '.')
print(yen_val)
yen_val = float(yen_val)

cny = 100
rub = cny * yen_val/yen_nom
print(round(rub, 2))
print(f'CN\u00A5{cny} = {round(rub, 2)}\u20BD') #юникод