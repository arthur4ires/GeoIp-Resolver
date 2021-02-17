import requests
import json
import socket
import sys

if (sys.argv[1] != "") == False:
	print('Seta o dns seu corno...')
	exit()

ipVerify = socket.gethostbyname(str(sys.argv[1]))

jsonResponse = requests.get('https://ipapi.co/' + ipVerify + '/json').json()


for x,y in enumerate(jsonResponse):
	print(y,jsonResponse[y])
