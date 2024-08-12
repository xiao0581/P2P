import requests
from os import listdir
from os.path import isfile, join
import threading
from socket import *
url = "https://actorrest220240228125032.azurewebsites.net/api/FileEndpoints"
ip="10.200.130.45"
port=2055
mypath = "C:/Users/xiaohui/Desktop/try"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for filename in onlyfiles:
    file={"filename":"test.txt," ,"ip":ip,"port":port }
    requests.post(url, json=file)

Server=socket(AF_INET,SOCK_STREAM)
Server.bind(("",port))
Server.listen(5)
print("Server ready for recive info")
def handle(connectionSocket,addr):
       filename = connectionSocket.recv(1024).decode().strip()
       filename=filename[4:]
       file = open('C:/Users/xiaohui/Desktop/try' + filename, 'rb')
       file_data = file.read(1024)
       while (file_data):
            print('Sending...')
            connectionSocket.send(file_data)
            file_data = file.read(1024)
       file.close()
       print("Done Sending")
       connectionSocket.shutdown(SHUT_WR)
       connectionSocket.close()
                     
while True:
    connectionSocket, addr = Server.accept()
    threading.Thread(target = handle,args = (connectionSocket,addr)).start()