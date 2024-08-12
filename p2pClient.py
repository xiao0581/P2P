import requests
import socket

url = "https://actorrest220240228125032.azurewebsites.net/api/FileEndpoints"

fileName = "test.exe"

response = requests.get(url + "?filename=" + fileName)
data = response.json()

serverIP = data[0]["ipAddress"]
serverPort = data[0]["port"]

my_socket = socket.socket()
my_socket.connect((serverIP, serverPort))
my_socket.send(("GET " + fileName).encode())

file = open('c:/temp/output/' + fileName, 'wb')

file_data = my_socket.recv(1024)
while (file_data):
    print("Receiving...")
    file.write(file_data)
    file_data = my_socket.recv(1024)
file.close()

print("Done Sending")
my_socket.close()