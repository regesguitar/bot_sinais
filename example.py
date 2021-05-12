from iqoptionapi.stable_api import IQ_Option
import time

API = IQ_Option('login', 'senha')
API.set_max_reconnect(3)
API.change_balance('PRACTICE') #PRACTICE/REALg

while True:
    if API.check_connect() == False:
        print('Erro ao conectar')
        API.reconnect()
    else:
        print('Conectado com sucesso')
        break

    time.sleep(1)

