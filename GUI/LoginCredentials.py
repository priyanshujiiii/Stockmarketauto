
print("Welcome to High Frequency Trading")
name1 = print('Enter your name')
#name = input()
#print('Welcome '+ name)
from  smartapi import SmartConnect
from smartapi import webSocket
import multiprocessing
import threading
print('CONNECTED WITH BSE AND NSE ')
apikey = "mfLIgnPz"
username1= print('Enter your userid')
username = 'P227148'
pws1 = print('Enter your pws')
pws = 'Priya@5163'
obj = SmartConnect(api_key=apikey)
data=obj.generateSession(username, pws)
refreshToken = data['data']['refreshToken']
feedToken = obj.getfeedToken()
userProfile = obj.getProfile(refreshToken)
