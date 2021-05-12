import json
from iqoptionapi.stable_api import IQ_Option
import logging
import time
import datetime as dt
import getpass
import json

asset = "EURUSD-OTC"
maxdict = 10
size = 300

logging.disable(level=(logging.DEBUG))



try:
	try_login = 0
	iq = {}
	status = False
	print("\nn\Informe o seu usuario e senha para iniciar\n")
	while status == False and try_login < 3:
		username = input("Usuário:")
		password = getpass.getpass("senha:")
		Iq = IQ_Option(username, password)
		try_login += 1
		status, reason = Iq.connect()
		if status == False:
			res = json.loads(reason)
			if "code" in res and res["code"] == "invalid_credentials":
				print("\nn\Erro ao conectar: Usuário ou senha incorreta\n\n")
			else:
				print("\nn\Erro ao conectar:" + 
					res["message"] + "\n\n")
		else:
			break
	if status == False:
		raise ValueError("Excedeu 3 tentativas. Tenta mais tarde novamente \n\n")

	print("Conectado com sucesso")
	MODE = "PRACTICE" #/"REAL
	Iq.change_balance(MODE)

except ValueError as value_error:
	print(value_error)
	print('Parando bot')

except KeyboardInterrupt:
	print("Parando bot")