from urllib.parse import urlencode
from urllib.request import Request, urlopen
import re
'''
url = 'https://rmsp.nalog.ru/search-proc.json' # Set destination URL here
post_fields = {'query': '999999999999999999999999'}     # Set POST fields here

request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)
'''


'''
{"pageCount":1,"dtQueryEnd":"18.03.2019 10:54:58","page":1,"pageSize":10,"data":[{"ogrn":"1092468017729","inn":"2466220319","isnew":0,"category":2,"regioncode":"24","dtregistry":"01.08.2016 00:00:00","nptype":"UL","okved1":"61.10.1","okved1name":"Деятельность по предоставлению услуг телефонной связи","citytype":"ГОРОД","cityname":"КРАСНОЯРСК","name_ex":"ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ \"ОРИОН ТЕЛЕКОМ\"","has_licenses":1,"has_contracts":0,"is_hitech":0,"is_partnership":0,"cnt":1,"token":"3C6BF6712E87C037B14C4E100E773E23E012D71FCE4705B983BABFD28D30C1ED683CCDE52FE48CA2AAEBF7AE5276BB78"}],"dtQueryBegin":"18.03.2019 10:54:58","queryCount":true,"rowCount":1,"rowLimit":0,"queryTime":2}
'''
'''
{"pageCount":1,"dtQueryEnd":"18.03.2019 11:04:34","page":1,"pageSize":10,"data":[{"ogrn":"1037700043732","inn":"7705031219","isnew":0,"category":3,"regioncode":"77","dtregistry":"10.08.2017 00:00:00","nptype":"UL","okved1":"64.19","okved1name":"Денежное посредничество прочее","name_ex":"АГРАРНЫЙ ПРОФСОЮЗНЫЙ АКЦИОНЕРНЫЙ КОММЕРЧЕСКИЙ БАНК \"АПАБАНК\" (АКЦИОНЕРНОЕ ОБЩЕСТВО)","has_licenses":1,"has_contracts":0,"is_hitech":0,"is_partnership":0,"cnt":1,"token":"49736EEEC9C66378379EAEC364752A5F1FF61102AF837E89588248B39A7492E4C07ADF92A107A57BE3B473A0690DA20E49E7B88DF5DFF68BD25F1B2AE8D57D9F"}],"dtQueryBegin":"18.03.2019 11:04:34","queryCount":true,"rowCount":1,"rowLimit":0,"queryTime":3}
'''
'''
{"pageCount":1,"dtQueryEnd":"18.03.2019 11:08:12","page":1,"pageSize":10,"data":[],"dtQueryBegin":"18.03.2019 11:08:12","queryCount":true,"rowCount":0,"rowLimit":0,"queryTime":3}
'''

def validate_inn_or_ogrn(value):
    p = re.compile('^[0-9]{9,}$')
    if not p.match(value):
        print('not')
    else:
        print(value)
validate_inn_or_ogrn('123467899')